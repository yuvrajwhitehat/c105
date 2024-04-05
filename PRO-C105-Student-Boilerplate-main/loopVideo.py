import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)
i=0
while True:
    index=i%(count-1)
    cv2.imshow("repeat",cv2.imread(images[index]))
    i=i+1
    if cv2.waitKey(29)==32:
        break
