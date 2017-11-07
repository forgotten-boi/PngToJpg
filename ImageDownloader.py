from PIL import Image
import os
from os import walk
from os import listdir
from os.path import isfile, join
import urllib.request



readFile = open("ImageUrl.txt", "r")
lines = readFile.readlines()
print(lines)
for url in lines:
    file_name = url.split('/')[-1]
    print(file_name)
    savelocation= 'save/' + file_name.strip('\n')
    print(savelocation) 
    urllib.request.urlretrieve(url, savelocation)

print(len(lines))
readFile.close()



