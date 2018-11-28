import os
import datetime

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from car.models import CarsAll, CarsIn
from parking_management_system.main import extract_license_plate



CAR_IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'car_img')


def index(request):
    return render(request, 'index.html')


@csrf_exempt
def upload_img(request):

    car_img = request.FILES.get('file_data', None)
    if not car_img:

        return HttpResponseRedirect('/index/')
    else:

        img_name = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S") + os.path.splitext(car_img.name)[1]
        car_img_path = os.path.join(CAR_IMG_DIR, img_name)

        with open(car_img_path, 'wb') as car_img_wb:
            for chunk in car_img.chunks():
                car_img_wb.write(chunk)
        return JsonResponse({
                        'success': True,
                        'img_name': img_name,
                      })


def info(request, img_name):
    plate_name = '%s_plate%s' % os.path.splitext(img_name)
    print('debug1')
    car_img_path = os.path.join(CAR_IMG_DIR, img_name)
    license_plate_path = os.path.join(CAR_IMG_DIR, plate_name)


    # bug
    car_license_plate = extract_license_plate(car_img_path,
                                              license_plate_path,
                                              'parking_management_system/textdetect-52e8d68b62cc.json')

    print('debug2')
    year, month, day, hour, minute, second = map(int, os.path.splitext(img_name)[0].split('_'))
    upd_time = datetime.datetime(year, month, day, hour, minute, second)


    query_result = CarsAll.objects.filter(license_id=car_license_plate).filter(exit_time=datetime.datetime(1970, 1, 1, 0, 0))

    print('debug3')
    if query_result:

        query_result.update(exit_time=upd_time)
        CarsIn.objects.filter(license_id=car_license_plate).delete()
        return render(request, 'info.html', {
            'car_img_path': '/car_img/' + img_name,
            'license_plate': car_license_plate,
            'entry_time': CarsAll.objects.filter(license_id=car_license_plate).order_by('-entry_time')[0].entry_time.strftime("%Y-%m-%d %H:%M:%S"),
            'exit_time': upd_time.strftime("%Y-%m-%d %H:%M:%S"),
            'cost': 1,
        })
    else:

        CarsAll.objects.create(license_id=car_license_plate, entry_time=upd_time, exit_time=datetime.datetime(1970, 1, 1, 0, 0))
        CarsIn.objects.create(license_id=car_license_plate, entry_time=upd_time)
        return render(request, 'info.html', {
            'car_img_path': '/car_img/' + img_name,
            'license_plate': car_license_plate,
            'entry_time': upd_time.strftime("%Y-%m-%d %H:%M:%S"),
            'exit_time': '',
            'cost': 1,
        })


def car_img(request, img_name):
    with open(os.path.join(CAR_IMG_DIR, img_name), 'rb') as img:
        return HttpResponse(img.read())
