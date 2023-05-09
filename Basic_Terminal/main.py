import insert
import calculate
import query
import delete
import os
import update
while True:               
    service = input("請選擇服務：新增資料請按1，查詢資料請輸入2，刪除資料請輸入3，更新程式請輸入4，離開程式請按5：")
    #利用break跳出while迴圈以退出程式
    if service =="5":
        print("感謝您的使用！")     
        break
    #新增資料
    elif service =="1":
    #輸入使用者的名字、身分證字號、性別、身高、體重、年紀等資料
        name = input("請輸入使用者名字：")    
        id = input("請輸入使用者身份證字號：")
        gender = int(input("請選擇性別，男生請輸入1，女生請輸入2："))
        height = int(input("請輸入身高(公分)："))
        weight = int(input("請輸入體重(公斤)："))
        age = int(input("請輸入年齡(單位：歲)："))
        calculate.cal(gender,height,weight,age)
        insert.new(name,id,gender,height,weight,age)
    elif service=="2":
        query.main()
    elif service=='3':
        name = input("請輸入欲刪除使用者名字：")
        id  = input("請輸入欲刪除使用者身份證字號：")
        delete.main(name,id)
    elif service == '4':
        name = input("請輸入要更新的使用者名字：")    
        id = input("請輸入要更新的使用者身份證字號：")
        update.up(name,id)
    else:
        print("無效指令")
os.system('pause')
        
        
        