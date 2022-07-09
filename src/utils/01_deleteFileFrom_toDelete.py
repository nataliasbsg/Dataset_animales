import os

# SOURCE = "D:/Animales/Lepóridos/00"
# SOURCE_txt = "D:/Animales/Lepóridos/00"

print('Enter the path to the images folder')
SOURCE = input()
print('Enter the path which contains the txt with the images to delete')
SOURCE_txt = input()


if not os.path.exists(SOURCE):
    print("Paht not exist")
    exit

if not SOURCE.endswith("/"):
    SOURCE += "/"

if not SOURCE_txt.endswith("/"):
    SOURCE_txt += "/"

if not os.path.exists(SOURCE_txt+"toDelete.txt"):
    print("Ejecuta primero el script checkSameImage")
    exit

lines = open(SOURCE_txt+"toDelete.txt").readlines()

for line in lines:
    line = line.replace("\n","")
    try:
        os.remove(SOURCE+line)
    except:
        print(SOURCE+line)
