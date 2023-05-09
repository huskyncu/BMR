import os
import calculate
import print_list
import tkinter as tk
from tkinter import ttk, messagebox
from gen import gen
def query(name,id):
    import pandas as pd
    df = pd.read_excel('data.xlsx')
    try:
        search = df.loc[(df['name']==name)&(df['id']==id)].to_dict(orient ='record')[0]
        if search['name']!="":
            return search,True
    except:
        return search,False
def main():

    def submit():
        name = name_text.get()
        id = id_text.get()
        #讀檔
        search,flag =query(name,id)
        if flag:
            contacts = []
            columns = ("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
            headers =("name","id", "gender",'height','weight','age','bmi','bmitype','idealweight','bmr','bmr_type')
            widthes = (80,80,80,80,80,80,80,80,90,80,80)
            tv = ttk.Treeview(query_wnd, show="headings",height=2 ,columns=columns)
            for (column, header, width) in zip(columns, headers, widthes):
                tv.column(column, width=width, anchor="w")
                tv.heading(column, text=header, anchor="w")
            print(search)
            def inser_data():
                """插入数据"""
                cal = calculate.cal(search['gender'],search['height'],search['weight'],search['age'])
                search['gender']=gen(search['gender'])
                contacts.append(tuple(search.values())+cal)
                for i, v in enumerate(contacts):
                    print(i,v)
                    tv.insert('', i,values=v)
            tv.place(relx=0.5,rely=0.35,anchor= 'n')
            inser_data()
            print("已完成查詢！")
            messagebox.showinfo("訊息","已完成查詢！")
        else:
            messagebox.showinfo("訊息","查無此人！")
    def close():
        query_wnd.destroy()
    query_wnd = tk.Tk()
    query_wnd.geometry("900x400")
    query_wnd.title("query_data")
    name_label  = tk.Label(query_wnd,text="請輸入名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(query_wnd)
    name_text.place(relx=0.6,rely=0.2,anchor= 'n')
    id_label = tk.Label(query_wnd,text="請輸入身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(query_wnd)
    id_text.place(relx=0.6,rely=0.25,anchor= 'n')
    submit_button= tk.Button(query_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.4, rely= 0.8, anchor = 'n')
    close_button= tk.Button(query_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.6, rely= 0.8, anchor = 'n')
    query_wnd.mainloop()

if __name__ == "__main__":
    main()