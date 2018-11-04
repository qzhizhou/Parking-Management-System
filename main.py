from license_plate_extraction import extraction
from googlevision import text

car_path = enter a car path 
license_plate_path = enter your save path
json_path = enter your json path

extraction.store_license_plate(car_path)
print(extraction.time_extraction(car_path))
text.recongnize(license_plate_path,json_path)
