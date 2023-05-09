import tkinter as tk
from tkinter import ttk,messagebox
from insert import new
from query import query
from delete import delete
def update_(dict):
    try:
        import pandas as pd
        df = pd.read_excel('data.xlsx')
        for k,v in dict.items():
            df.loc[df['name'] ==dict['name'], k] = v
        df.to_excel('data.xlsx',index=False)
        return True
    except:
        return False
def update():
    def submit():
        def up():
            name = name_text.get()
            id = id_text.get()
            weight = weight_text.get()
            height = height_text.get()
            age = age_text.get()
            gender_str = onthchoosen.get()
            if gender_str == "男生":
                gender = '1'
            else:
                gender = '2'
            if update_({"name":name,"id":id,"gender":gender,"height":height,"weight":weight,"age":age}):
                messagebox.showinfo('訊息','更新完畢')
                print('已更新完畢')
                update_wnd.destroy()
            else:
                print('查無此人')
                messagebox.showinfo('訊息','查無此人')
        name = name_text.get()
        id = id_text.get()
        Has = False
        search ,Has = query(name,id)
        if Has:
            gender_label  = tk.Label(update_wnd,text="請選擇性別:")
            gender_label.place(relx=0.25,rely=0.3,anchor="n")
            n = tk.StringVar()
            onthchoosen = ttk.Combobox(update_wnd, width = 17, textvariable = n)
            onthchoosen['values'] = ('男生', '女生')
            onthchoosen.place(relx=0.65,rely=0.3,anchor="n")
            height_label  = tk.Label(update_wnd,text="請輸入身高(單位：公分):")
            height_label.place(relx=0.25,rely=0.35,anchor="n")
            height_text = tk.Entry(update_wnd)
            height_text.place(relx=0.65,rely=0.35,anchor= 'n')
            weight_label = tk.Label(update_wnd,text="請輸入體重(單位：公斤):")
            weight_label.place(relx=0.25,rely=0.4,anchor="n")
            weight_text = tk.Entry(update_wnd)
            weight_text.place(relx=0.65,rely=0.4,anchor= 'n')
            age_label = tk.Label(update_wnd,text="請輸入年齡:")
            age_label.place(relx=0.25,rely=0.45,anchor="n")
            age_text = tk.Entry(update_wnd)
            age_text.place(relx=0.65,rely=0.45,anchor= 'n')
            update_button= tk.Button(update_wnd,text='update',command = up,underline=-1)
            update_button.place(relx= 0.6, rely= 0.6, anchor = 'n')
        else:
            messagebox.showinfo("訊息","查無此人！")
                        
    def close():
        update_wnd.destroy()
    update_wnd = tk.Tk()
    update_wnd.geometry("400x400")
    update_wnd.title("update_data")
    name_label  = tk.Label(update_wnd,text="請輸入欲更新的名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(update_wnd)
    name_text.place(relx=0.65,rely=0.2,anchor= 'n')
    id_label = tk.Label(update_wnd,text="請輸入欲更新的身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(update_wnd)
    id_text.place(relx=0.65,rely=0.25,anchor= 'n')
    submit_button= tk.Button(update_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.3, rely= 0.6, anchor = 'n')
    close_button= tk.Button(update_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.9, rely= 0.6, anchor = 'n')
    update_wnd.mainloop()

if __name__ == "__main__":
    update()