from license_image_extraction import extraction
from recognize_license_id import *
import pymysql
import pymysql

'''
import pandas as pd
import numpy as np
import MySQLdb'''

car_path = "/Users/gangwei/Desktop/smartparker/car_image/car2.jpg"
license_plate_path = '/Users/gangwei/Desktop/smartparker/license_image/license2.jpg'
json_path = "/Users/gangwei/Desktop/smartparker/textdetect-52e8d68b62cc.json"

upd_time = extraction.time_extraction(car_path)
extraction.store_license_plate(car_path,license_plate_path)
license_id = text.recognize(license_plate_path, json_path)
print(upd_time)
print(license_id)
print("Processing Database")
balance = 300


def entry_cars_all():

    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "INSERT INTO cars_all(license_id, entry_time, balance) VALUES(\'%s\', \'%s\', \'%s\')" % (
        license_id, upd_time, balance)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def entry_cars_in():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "INSERT INTO cars_in(license_id, entry_time, balance) VALUES(\'%s\', \'%s\', \'%s\')" % (
        license_id, upd_time, balance)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def entry_cars_balance():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "INSERT INTO cars_balance(license_id, balance) VALUES(\'%s\', \'%s\')" % (
        license_id, balance)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def  out_cars_all():

    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "UPDATE cars_all SET exit_time = '%s' WHERE license_id = '%s'" % (upd_time,license_id)

    #try:
    cursor.execute(sql)
    db.commit()
    '''except:
        db.rollback()
        db.close()'''

def out_cars_in():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "DELETE FROM cars_in WHERE license_id = '%s'" % (license_id)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def out_cars_balance():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "UPDATE cars_balance SET balance = balance - 1 WHERE license_id = '%s'" % (license_id)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

#if(entry==1):
#entry_cars_all()
#entry_cars_in()
#entry_cars_balance()

#if(out==1):
#out_cars_in()
#out_cars_all()
#out_cars_balance()
