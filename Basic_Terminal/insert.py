def new(name,id,gender,height,weight,age):
    with open('data.txt', mode='a+') as patient_file:
      patient_file.write(name+" "+id+" "+str(gender)+" "+str(height)+" "+str(weight)+" "+str(age)+"\n")
    print(name+"的資料新增成功")