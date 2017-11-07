from PIL import Image
import os
from os import walk
from os import listdir
from os.path import isfile, join


# 
outputdir = "D:/Javra/Research/ObjectDetectionTensorflowSharp/PngTOJpg/Image/truckjpg/" 
directoryPath = "D:/Javra/Research/ObjectDetectionTensorflowSharp/PngTOJpg/Image/truck"
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]




f = []

for (dirpath, dirnames, filenames) in walk(directoryPath):
    f.extend(filenames)
    break

for filen in f:
    im = Image.open(directoryPath + '/'+ filen)
    rgb_im = im.convert('RGB')
    imageName = os.path.splitext(filen)[0]
    rgb_im.save(outputdir + imageName + '.jpg')

#     
#     break

