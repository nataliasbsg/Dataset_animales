import os
from PIL import Image

# SOURCE = "D:/Animales/Lepóridos/00"
# OUTPATH = "D:/Animales/Lepóridos/00"

print('Enter the path to the images folder')
SOURCE = input()
print('Enter the path to save the txt with the images to delete')
OUTPATH = input()

mode = 1 # 0, compara nombres, 1 compara las imágenes con PIL

IMAGE_EXT = [".jpg", ".jpeg", ".png", ".bmp"]


if not os.path.exists(SOURCE):
    print("Paht not exist")
    exit

if not SOURCE.endswith("/"):
    SOURCE += "/"

if not OUTPATH.endswith("/"):
    OUTPATH += "/"

files = os.listdir(SOURCE)
filesToDelete = []
for n_file in range(len(files)):
    fileName, extension = os.path.splitext(files[n_file])
    print("[{}/{}]".format(n_file,len(files)))
    if mode == 0:
        for n_compare in range(len(files)):
            if n_compare != n_file:
                if fileName in files[n_compare]:
                    filesToDelete.append(files[n_compare])
    if mode == 1:
        if extension.lower() not in IMAGE_EXT: continue
        image = Image.open(SOURCE+files[n_file])
        for n_compare in range(n_file+1, len(files)):
            if os.path.splitext(files[n_compare])[1].lower() in IMAGE_EXT:
                image_compare = Image.open(SOURCE+files[n_compare])
                if image == image_compare:
                    filesToDelete.append(files[n_compare])

if len(filesToDelete) != 0:
    text = ""
    for _fileToDelete in filesToDelete:
        text += _fileToDelete + "\n"
    toDelete = open(OUTPATH+"toDelete.txt", 'w')
    toDelete.write(text)
    toDelete.close