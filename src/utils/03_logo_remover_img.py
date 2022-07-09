from PIL import Image
import os
import cv2
import numpy as np
from tqdm import tqdm

print('Enter the path to the images folder')
dir_bd = input()
files = os.listdir(dir_bd)
print('Enter the path to save the images')
dir_dest = input()

if not os.path.exists(dir_dest):
  os.mkdir(dir_dest)

for file in tqdm(os.listdir(dir_bd)):
    try:
        img = cv2.imread(f'{dir_bd}/{file}',1)
        x, y, z = np.shape(img)
        # print(x,y,z)
        # Los parametros x0, x1, y0, y1 tienen que adaptarse a la posicion del logo
        x0 = int(y/30) 
        x1 = int(y/10) 
        y0 = int(y/30) 
        y1 = int(y/10) 

        b, g, r = img[int((y0+y1)/2), int(x1+10)]
        # b0, g0, r0 = im[int((y00+y01)/2), int(x00-10)]
        
        bgr = (int(b),int(g),int(r))
        # bgr0 = (int(b0),int(g0),int(r0))

        cv2.rectangle(img,(x0, y0),(x1, y1),bgr,-1) #rtve
        # cv2.rectangle(im,(x00, y00),(x01, y01),bgr0,-1) #rtve

        # Create ROI coordinates
        topLeft = (x0-10,y0-10)
        bottomRight = (x1+10,y1+10)
        # topLeft = (x00-10,y00-10)
        # bottomRight = (x01+10,y01+10)

        x, y = topLeft[0], topLeft[1]
        w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

        # Grab ROI with Numpy slicing and blur
        ROI = img[y:y+h, x:x+w]
        blur = cv2.GaussianBlur(ROI, (51,51), 0) 

        # Insert ROI back into imageBB
        img[y:y+h, x:x+w] = blur

        cv2.imwrite(f'{dir_dest}/{file}', img) 

    except:
        print('El logo no se ha podido borrar de la imagen', file)
        pass