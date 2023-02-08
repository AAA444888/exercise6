import os
def search(nid):
    if os.path.exists(nid+".txt"):
        with open(nid+".txt",mode='r') as file:
            name = file.readline()
            nid = file.readline()
            age = file.readline()
            height = file.readline()
            weight = file.readline()
            print(nid + "電子健康檔案如下：")
            print("姓名：" + name.replace('\n',''))
            print("年紀：" + age.replace('\n',''))
            print("身高：" + height.replace('\n',''))
            print("體重：" + weight.replace('\n',''))
    else:
        print("找不到檔案")