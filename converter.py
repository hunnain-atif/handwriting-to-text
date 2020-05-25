import os, io
from google.cloud import vision
from google.cloud.vision import types
import pandas as pd 

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'googleServiceAccountKey.json'
client = vision.ImageAnnotatorClient()

image_folder = input("Enter image folder path: ")
FOLDER_PATH = image_folder

name_image = input("Enter the file name: ")
IMAGE_NAME = name_image

FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_NAME)

with io.open(FILE_PATH, 'rb') as input_file:
    content = input_file.read()

image = vision.types.Image(content=content)
response = client.document_text_detection(image=image)

documentText = response.full_text_annotation.text 


if os.path.exists("convertedText.txt"):
  os.remove("convertedText.txt")

output_file = open("convertedText.txt", "x")
output_file.write(documentText)
output_file.close()

print("successfully translated image to text... look at convertedText.txt file" )
