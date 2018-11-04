# Parking-Management-System
This is to build a system that can self detect the car plates and calculate the parking fee. We have realised the function to capture the license plate from a car photo. As for character recognition, our original method CCA would make some mistakes when the photo is not quite clear. It can not segment each charcater from others due to the crack the charcters may have in themselves, so we only use CCA as a method to detect license plates. Our decision is to use google vision to recongnise charcters on the license plates. 

## First install the required library

    pip install -r requirements.txt 

## Second run main.py program
    python main.py

## What to do
    You should enter your image path of the cars taken by cameras,(Entry & Exit), 
    your google_vision json path, and the storage path of the images of the license plate, 
    extracted by the program 'license-plate-extraction'.
