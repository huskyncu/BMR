import tkinter as tk
from tkinter import ttk,messagebox
from query import query
def delete(search):
    import pandas as pd
    try:
        df = pd.read_excel('data.xlsx')
        df = df.drop(search.index)
        df.to_excel('data.xlsx',index=False)
        return True
    except:
        return False
def main():
    def submit():
        name = name_text.get()
        id = id_text.get()
        flag = False
        search, flag = query(name,id)
        if flag:
            if delete(search):
                messagebox.showinfo('訊息','刪除成功！')
                close()
            else:
                messagebox.showinfo('訊息','刪除失敗！')
        else:
            print("查無此人！")
            messagebox.showinfo('訊息','查無此人！')
    def close():
        delete_wnd.destroy()
    delete_wnd = tk.Tk()
    delete_wnd.geometry("400x400")
    delete_wnd.title("delete_data")
    name_label  = tk.Label(delete_wnd,text="請輸入欲刪除的使用者名字:")
    name_label.place(relx=0.25,rely=0.2,anchor="n")
    name_text = tk.Entry(delete_wnd)
    name_text.place(relx=0.7,rely=0.2,anchor= 'n')
    id_label = tk.Label(delete_wnd,text="請輸入該使用者的身分證字號:")
    id_label.place(relx=0.25,rely=0.25,anchor="n")
    id_text = tk.Entry(delete_wnd)
    id_text.place(relx=0.7,rely=0.25,anchor= 'n')
    submit_button= tk.Button(delete_wnd,text='submit',command = submit,underline=-1)
    submit_button.place(relx= 0.4, rely= 0.8, anchor = 'n')
    close_button= tk.Button(delete_wnd,text='close',command = close,underline=-1)
    close_button.place(relx= 0.6, rely= 0.8, anchor = 'n')
    delete_wnd.mainloop()
if __name__ == "__main__":
    main()