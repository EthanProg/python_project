import datetime
import os
import shutil
from hashlib import md5

import cv2
import numpy as np

ORIGINAL_PATH = "E:/imgdownload/imgdist/1.6/源文件"
AFTER_PATH = "E:/imgdownload/imgdist/1.6/目标文件"
CANT_DEAL_PATH = "E:/imgdownload/imgdist/1.6/未处理文件"
PICHASH = {}


def get_file(name):
    parent_file_path = os.listdir(name)
    child = []
    for file_path in parent_file_path:
        child_path = name + "/" + file_path
        child.append(child_path)
    return child


def deal_img(imgFile):
    try:
        #img = cv2.imread(imgFile.encode('gbk'),1)
        img = cv2.imdecode(np.fromfile(imgFile,dtype=np.uint8), -1)
        x, y, z = img.shape  # 高 宽  通道数
        cant_deal_file_path = imgFile.replace("源文件", "未处理文件")
        # if x < 600 and y < 1000:  # 太小文件不处理
        #     shutil.copyfile(imgFile, cant_deal_file_path)
        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + imgFile + "文件太小，跳过")
        # if y > 3500:  # 太大的文件不处理
        #     shutil.copyfile(imgFile, cant_deal_file_path)
        #     print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "," + imgFile + "文件太大，跳过")
        if os.path.exists(imgFile):  # 这就是最关键的代码了
            print(imgFile)
            for i in range(int(x/13)):
                for j in range(int(y/3.15)+10):
                    varP = img[i, j]
                    img[i, j] = img[int(i/12.5), j]
                    # if sum(varP) > 556 and sum(varP) < 640:  # 大于250，小于765（sum比白色的小）
                    #     #img[i, j] = img[i - 5, j - 10]
                    #
                    #     print(img[i, j])
            dst = imgFile.replace("源文件", "目标文件")
            #shutil.copyfile(imgFile, dst)
            #cv2.imwrite(dst, img)
            #cv2.imread(imgFile.decode('u8').encode('gbk'), -1)
            cv2.imencode('.jpg', img)[1].tofile(dst)
            #hutil.copyfile(imgFile, dst)
            #shutil.copyfile(imgOldFile, imgOldFile)

    except Exception as e:
        shutil.copyfile(imgFile, cant_deal_file_path)
        print("Exception:", e)


if __name__ == '__main__':
    or_path = get_file(ORIGINAL_PATH)
    for path in or_path:
        for fileName in os.listdir(path):
            img_path = path+"/"+fileName
            # print(img_path)
            deal_img(img_path)

