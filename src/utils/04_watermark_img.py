#Importar librería cv2
import cv2
import os
from tqdm import tqdm

print('Introduce la direccion carpeta con las imagenes a las que quieres insertar la marca de agua')
dir_folder = input()
print('Introduce la direccion carpeta para almacenar la imagenes (no hace falta que exista)')
dir_new_folder = input()
print('Introduce el texto de la marca de agua')
texto = input()

#Características del texto 1
colorLetra = (0,0,0) #(109,131,238)
#Características del texto 2
colorLetra2 = (255,255,255)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

if not os.path.exists(dir_new_folder):
  os.mkdir(dir_new_folder)

for image in tqdm(os.listdir(dir_folder)):
    
    #Leer imagen
    img = cv2.imread(dir_folder + '/{}'.format(image))
    h, w, c = img.shape
    ubicacion = (int(w/30),int(h-(w/30)))
    tamañoLetra = h/700 #1400
    grosorLetra = int(h/300)
    grosorLetra2 = int(h/1200)

    #Escribir texto
    cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra, grosorLetra)
    cv2.putText(img, texto, ubicacion, font, tamañoLetra, colorLetra2, grosorLetra2)

    #Guardar imagen
    cv2.imwrite(dir_new_folder + '/{}'.format(image), img)


    # #Mostrar imagen
    # cv2.imshow('imagen',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
