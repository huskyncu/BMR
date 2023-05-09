import print_list
def up(name,id):
    data = []
    flag = False
    with open('data.txt', mode='r') as patient_file:
      for line in patient_file.readlines():
        line_obj = line.split()
        data.append(line_obj)
    for i in range(len(data)):
        if data[i][0]==name and data[i][1]==id:
            print_list.printout(data[i])
            del data[i]
            gender = input("請選擇新的性別，男生請輸入1，女生請輸入2：")
            height = input("請輸入新的身高(公分)：")
            weight = input("請輸入新的體重(公斤)：")
            age = input("請輸入新的年齡(單位：歲)：")
            line=[name,id,gender,height,weight,age]
            data.append(line)
            flag = True
            print("更新完成！")
            break
    if flag:
        with open('data.txt', mode='w') as patient_file:
            for line in data:
                name,id,gender,height,weight,age = line[0],line[1],line[2],line[3],line[4],line[5]
                patient_file.write(name+" "+id+" "+gender+" "+height+" "+weight+" "+age+"\n")
    else:
        print("查無此人！")