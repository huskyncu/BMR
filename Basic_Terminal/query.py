import os
import calculate
import print_list
def main():
    global has
    has = False
    if os.path.exists("data.txt"):
        name = input("請輸入使用者的名字：")
        id = input("請輸入使用者的身份證字號：")
        #讀檔
        with open('data.txt',mode='r') as patient_file:
            #先讓完檔案所有東西後，再去跑每一行的內容。
            lines = patient_file.readlines()
            for line in lines:
                # 因為讀進來是一整個字串，我把它先換成list，方便我後面的操作。
                line_obj = line.split()
                # 如果name跟id都符合該行資料的第一個資料跟第二個資料，那就執行裡面的程式。
                if line_obj[0]==name and line_obj[1]==id:
                    # 找到了。
                    has = True
                    # 一個一個印出資料
                    print_list.printout(line_obj)
                    # 我先把list的資料str型態轉型成int型態，這樣方便我後續幾行傳入函式的的操作。
                    gender = int(line_obj[2])
                    height = int(line_obj[3])
                    weight = int(line_obj[4])
                    age = int(line_obj[5])
                    calculate.cal(gender,height,weight,age)
                    print("已完成查詢！")
                    #因為執行完了，我就跳出迴圈。
                    break
            if has == False:
                print("查無此人！")
    else:   
        print("沒有資料，請先新增資料！")