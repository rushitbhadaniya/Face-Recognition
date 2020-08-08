# -*- coding: utf-8 -*-
"""face_recognition.ipynb

Automatically generated by Colaboratory.

Author : Rushit Bhadaniya

Original file is located at
    https://colab.research.google.com/drive/1pttVU9nIvIH_K-K2b7Z6aeZvdDkAWHvx
"""

pip install face_recognition

#pip install Dlib

import PIL.Image
import PIL.ImageDraw
import face_recognition

!nvidia-smi

image = face_recognition.load_image_file("rushit.jpeg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

number_of_faces = len(face_locations)
print("I found {} face(s) in this photograph.".format(number_of_faces))

# Load the image into a Python Image Library object so that we can draw on top of it and display it
pil_image = PIL.Image.fromarray(image)
n=1
ext='.jpg'
for face_location in face_locations:

    # Print the location of each face in this image. Each face is a list of co-ordinates in (top, right, bottom, left) order.
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # Let's draw a box around the face
    draw = PIL.ImageDraw.Draw(pil_image)
    draw.rectangle([left, top, right, bottom], outline="red")
    img=pil_image.crop((left,top,right,bottom))
    img.save('person_'+str(n)+ext,)
    n+=1
    

# Display the image on screen
pil_image.show()

