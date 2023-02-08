def add(name,nid,age,height,weight):
    with open(nid+".txt",mode='w') as file:
        file.write(name + "\n"+nid + "\n"+age + "\n"+height + "\n"+weight + "\n")
    print("檔案新增成功")