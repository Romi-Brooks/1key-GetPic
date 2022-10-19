import os
import time
import wget
from datetime import datetime

Url = "https://iw233.cn/api.php?sort=random"

print("api来自MirlKoi,单个ip在60s请求120次会被拉黑")
print("因此做了延迟,每5s下载一次")

if not os.path.exists("img"):
    os.mkdir("img")
    print("创建img文件夹成功")
    print("文件将下载到img文件夹中")
else:
    print("文件将下载到img文件夹中")

def getFileName():
    dt02 = datetime.today()
    return dt02.strftime("%Y-%m-%d-%H-%M-%S") + ".jpg"

def downloadFile():
    while True:
        print("开始下载")
        file_name = wget.download(Url, out=getFileName())
        print("\n文件名: ", getFileName())
        os.rename(file_name, "img/" + file_name)
        time.sleep(5)

downloadFile()