def main(name,id):
    data = []
    flag = False
    with open('data.txt', mode='r') as patient_file:
      for line in patient_file.readlines():
        line_obj = line.split()
        data.append(line_obj)
    for i in range(len(data)):
        if data[i][0]==name and data[i][1]==id:
            del data[i]
            print("刪除成功！")
            flag = True
            break
    if flag:
        with open('data.txt', mode='w') as patient_file:
            for line in data:
                name,id,gender,height,weight,age = line[0],line[1],line[2],line[3],line[4],line[5]
                patient_file.write(name+" "+id+" "+gender+" "+height+" "+weight+" "+age+"\n")
    else:
        print("查無此人！")