from PIL import Image
import imagehash
import os
import cv2
path = 'D:/Bishe/mid_term/scene'
# 以防万一
# def getfilesname(path):
#     filesname =[]
#     if(path != '' and path != ()):
#         for filename in os.listdir(path):   
#             for picname in os.listdir(path+'/'+filename):
#                 if os.path.splitext(picname)[1] == ".jpg" or os.path.splitext(picname)[1] == ".png" or os.path.splitext(picname)[1] == ".JPG" or os.path.splitext(picname)[1] == ".jpeg" :
#                     filesname+=[path+'/'+filename+'/'+picname]
#                     break          
#     else:
#         filesname = []
#     return filesname



def getfilesname(path):
    filesname =[]
    if(path != '' and path != ()):
        sceneids = os.listdir(path)
        for i in sceneids:
            if os.path.splitext(i)[1] == ".jpg" or os.path.splitext(i)[1] == ".png" or os.path.splitext(i)[1] == ".JPG" or os.path.splitext(i)[1] == ".jpeg" :
                filesname+=[path+'/'+i]
    else:
        filesname = []
    return filesname


filesname = getfilesname(path)
# print(len(filesname))


hash = imagehash.phash(Image.open('B_076.jpg'))
print(hash)
max = 100
string = ''
for i in range(len(filesname)):

    otherhash = imagehash.phash(Image.open(filesname[i]))
    #print(hash - otherhash)
    if(hash-otherhash< max):
        max = hash-otherhash
        string = filesname[i]
print(string)

cv2.imshow('1',cv2.resize(cv2.imread(string),(1000,750)))
cv2.waitKey(0)