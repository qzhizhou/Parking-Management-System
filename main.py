from license_image_extraction import extraction
from recognize_license_id import *
import pymysql
import pymysql

'''
import pandas as pd
import numpy as np
import MySQLdb'''

car_path = "/Users/gangwei/Desktop/smartparker/car_out_image/car6.jpg"
license_plate_path = '/Users/gangwei/Desktop/smartparker/license_image/license6.jpg'
json_path = "/Users/gangwei/Desktop/smartparker/textdetect-52e8d68b62cc.json"

upd_time = extraction.time_extraction(car_path)
extraction.store_license_plate(car_path,license_plate_path)
license_id = text.recognize(license_plate_path, json_path)
print(upd_time)
print(license_id)
print("Processing Database")



def entry_cars_all():

    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "INSERT INTO cars_all(license_id, entry_time, image_path) VALUES(\'%s\', \'%s\', \'%s\')" % (
        license_id, upd_time, car_path)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def entry_cars_in():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    sql = "INSERT INTO cars_in(license_id, entry_time) VALUES(\'%s\', \'%s\')" % (
        license_id, upd_time)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

def entry_cars_balance():
    balance = input("Give me the money:")
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

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
        db.close()

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

def query():
    db = pymysql.connect("localhost", "root", "WeiGang0502", "smartparker")
    cursor = db.cursor()
    #l_id = input("The license you want to find is: ")
    sql = "SELECT * FROM cars_all \
           WHERE No. = '%s'" % (7)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            license_id = row[1]
            entry_time = row[2]
            exit_time = row[3]
            image_path = row[5]
            print("license_id='%s',entry_time='%s',exit_time='%s',image_path='%s'" % \
                  (license_id, entry_time, exit_time, image_path))
    except:
        print("Error: unable to fetch data")
    db.close()

#if(entry==1):
#entry_cars_all()
#entry_cars_in()
#entry_cars_balance()

#if(out==1):
out_cars_in()
out_cars_all()
out_cars_balance()
#query()
