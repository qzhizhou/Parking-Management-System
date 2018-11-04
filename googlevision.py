# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:00:36 2018

@author: 41410
"""


import io
from google.cloud import vision
import os

class text():
    def recongnize(image_path,json_path):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=json_path
        client = vision.ImageAnnotatorClient()
        
        with io.open(image_path,'rb') as image_file:
            content = image_file.read()
        
        image = vision.types.Image(content=content)
        
        response = client.text_detection(image=image)
        texts = response.text_annotations
        #print('Texts:')
        #print('\n"{}"'.format(texts.description))
        for text in texts:
            print(text.description)

#    vertices = (['({},{})'.format(vertex.x, vertex.y)
#                    for vertex in text.bounding_poly.vertices])

#    print('bounds: {}'.format(','.join(vertices)))