###########################################################################################################################################
# LIBRERIAS

# Tratamiento de imagenes
import numpy as np
import cv2
import os

# Carpeta raiz
# dir = os.path.dirname(os.path.realpath(__file__))

# dir_bd = dir + 'bd_tester'
# dir_bd = dir + '/bd_tester_little'

print('Enter the path to the images folder')
dir_bd = input()

print('Enter the path to save the images')
dir_dest = input()

if not os.path.exists(dir_dest):
    os.makedirs(dir_dest)

for img_name in  os.listdir(dir_bd):
    img = cv2.imread(dir_bd + '/' + img_name)
    img = cv2.resize(img, (224,224))
    cv2.imwrite(f"{dir_dest}/{img_name}", img)

############################################################################################################################################
