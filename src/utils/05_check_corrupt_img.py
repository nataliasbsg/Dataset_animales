import os
from PIL import Image
# from time import sleep
from tqdm import tqdm

# dir_train = 'G:/Mi unidad/Colab Notebooks/BD_Familia'

print('Enter the path to the images folder')
dir_train = input()

categories = sorted(os.listdir(dir_train))
print (categories)
categories_folders = [os.path.join(dir_train, categorie) for categorie in categories]
subcategories = []
for categorie in categories:
    subcategories.append(sorted(os.listdir(dir_train+'/{}'.format(categorie))))
    for subcategorie in subcategories[categories.index(categorie)]:
        print(categorie +'/'+ subcategorie)
        listImages = os.listdir(dir_train+'/{}/{}'.format(categorie,subcategorie))
        for img in tqdm(listImages):
            imgPath = os.path.join(dir_train+'/{}/{}'.format(categorie,subcategorie),img)  
               
            try:
                # print(img)
                img = Image.open(imgPath)
                exif_data = img._getexif()
                img.close()
            except:
                img.close()
                print("+++++++++++++++++++++")
                print("Error on image: ", img)
                print("Subcategorie: ", subcategorie)
                os.remove(imgPath)