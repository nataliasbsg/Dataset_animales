###########################################################################################################################################
# LIBRERIAS

# Tratamiento de imagenes
import numpy as np
import cv2
import os
from tqdm import tqdm

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

for categorie in os.listdir(dir_bd):
  for subcategorie in os.listdir(f'{dir_bd}/{categorie}'):
    print (f'\n{categorie}/{subcategorie}')
    if not os.path.exists(f"{dir_dest}/{categorie}/{subcategorie}"):
        os.makedirs(f"{dir_dest}/{categorie}/{subcategorie}")
    for img_name in  tqdm(os.listdir(f'{dir_bd}/{categorie}/{subcategorie}')):
        img = cv2.imread(f'{dir_bd}/{categorie}/{subcategorie}/{img_name}')
        img = cv2.resize(img, (299,299))
        cv2.imwrite(f"{dir_dest}/{categorie}/{subcategorie}/{img_name}", img)

############################################################################################################################################
