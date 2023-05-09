import os
import calculate
import print_list
import tkinter as tk
import pymysql
from tkinter import ttk, messagebox
import db_dict
import csv


def download():
    db_setting = db_dict.dict()
    conn = pymysql.connect(**db_setting)
    try:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM bmr_chart")
        line = cursor.fetchall()
        new_list = []
        for i in range(len(line)):
            new_list.append( list(line[i]))
            if new_list[i][3]==1:
                new_list[i][3]='男'
            else:
                new_list[i][3]='女'
        conn.commit()
        with open('data.csv','w',newline='',encoding='UTF-8-Sig') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerow(['num','id','name','gender','體重','身高','年紀'])
            mywriter.writerows(new_list)
        print("已下載資料！")
        messagebox.showinfo("訊息","已下載資料！")
    except:
        messagebox.showinfo("訊息","查無資料！")
        