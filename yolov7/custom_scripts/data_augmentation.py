import cv2
import numpy
import os
import glob
from matplotlib import pyplot as plt
import albumentations as A
import random


class generateData():
    def __init__(self):
        self.options = [
                    A.VerticalFlip(p=1.0),
                    A.HorizontalFlip(p=1.0),
                    A.Transpose(p=1.0),
                    A.HueSaturationValue(p=1.0),
                    A.RandomBrightnessContrast(p=1.0),
                    A.RandomRotate90()]

        self.id_ = 0
    
    def augmentData(self, all_img_path, img_save_path, txt_save_path):
        if not os.path.exists(img_save_path):
          os.makedirs(img_save_path)
        if not os.path.exists(txt_save_path):
          os.makedirs(txt_save_path)
        all_img = glob.glob(all_img_path + "/*.png")
        for aug in self.options:
    
            for image in all_img: 
                img = cv2.imread(image)
                image_name = image.split("/")[-1].split(".")[0]

                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


                H, W = img.shape[0], img.shape[1]

                txt = image.replace("images", "labels").replace(".png", ".txt")

                with open(txt, "r") as f:
                    data = f.read()
                    data = data.split("\n")

                finalData = []

                for bbox in data:
                    if bbox != "":
                        new_bbox = bbox.split(" ")
                        x,y,w,h = float(new_bbox[1]), float(new_bbox[2]), float(new_bbox[3]), float(new_bbox[4])
                        finalData.append([x,y,w,h, 'dump'])

                transform = A.Compose([aug], bbox_params=A.BboxParams(format='yolo'))
                transformed = transform(image=img, bboxes=finalData)

                transformed_image = transformed['image']
                rgb_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)
                cv2.imwrite(f"{img_save_path}{image_name}_{self.id_}.png", rgb_image)


                transformed_bboxes = transformed['bboxes']

                for new_bbox in transformed_bboxes:
                    center_X = new_bbox[0]
                    center_y = new_bbox[1]
                    width = new_bbox[2]
                    height = new_bbox[3]

                    with open(f"{txt_save_path}{image_name}_{self.id_}.txt", 'a') as f1:
                        f1.write(f'0 {center_X} {center_y} {width} {height} \n')


            self.id_ += 1