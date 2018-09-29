# -*- coding : UTF-8 -*-

import http.client
import hashlib
import json
import urllib
import random
import os
import base64
from PIL import ImageTk
import PIL
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter as tk
from in_ico import img

class user(Frame) :
    def __init__(self, root1) :
        frame = Frame(root1)
        frame.place(x = 0, y = 0, width = 600, height = 600)
        self.lab1 = Label(frame, text='输入:')
        self.lab2 = Label(frame, text='源语言:')
        self.lab3 = Label(frame, text='目标语言:')
        self.lab4 = Label(frame, text = '译文:')
        self.en1 = Entry(frame, width = 40) #输入
        self.en2 = Entry(frame, width = 40) #译文
        self.cho1 = ttk.Combobox(frame, width = 10, textvariable = cho_bef)
        self.cho2 = ttk.Combobox(frame, width = 10, textvariable = cho_aft)
        self.but1 = Button(frame, text = '翻译', command = self.translate)
        self.but2 = Button(frame, text = '重置', command = self.clean)
        self.but3 = Button(frame, text = '退出', command = root1.quit)
        self.place()
        self.displaying = False
    
    def clean(self) :
        self.en1.delete(0, END)
        self.en2.delete(0,END)
    
    def place(self) :
        self.cho1['values'] = ('en(英语)', 'zh(中文)', 'jp(日文)', 'auto(自动检测)')
        self.cho2['values'] = ('zh(中文)', 'en(英语)', 'jp(日文)')
        self.cho1.current(0)
        self.cho2.current(0)
        self.lab1.place(x = 20, y = 20) #输入
        self.lab2.place(x = 30, y = 160)    #源语言
        self.lab3.place(x = 180, y = 160)   #目标语言
        self.lab4.place(x = 20, y = 60) #译文
        self.en1.place(x = 60, y = 20)  #输入
        self.en2.place(x = 60, y = 60)  #译文
        self.cho1.place(x = 80, y = 160) #源语言
        self.cho2.place(x = 240, y = 160)    #目标语言
        self.but1.place(x = 80, y = 100)    #翻译
        self.but2.place(x = 180, y = 100)   #重置
        self.but3.place(x = 280, y = 100)   #退出
        
    def translate(self):
        self.en2.delete(0,END) 
        appid = '20180723000188375'
        secretKey = 'xzhDoXyUygCjKhLEwTDe'
        httpClient = None
        myurl = '/api/trans/vip/translate'
        q = self.en1.get()
        fromLang = self.cho1.get() # 源语言
        toLang = self.cho2.get()    # 翻译后的语言
        if (fromLang[:5] == 'auto') : fromLang = 'auto'
        else : fromLang = fromLang[:2]
        toLang = toLang[:2]
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = (myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign)
        
 
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            jsonResponse = response.read().decode("utf-8")# 获得返回的结果，结果为json格式
            js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
            dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
            self.en2.insert(0, dst) # 打印结果
        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()
        

def use() :
    
    tmp = open('in.ico', 'wb')
    tmp.write(base64.b64decode(left))
    tmp.close()
    
    root.destroy()
    root1 = Tk()
    root1.title('translate')
    root1.iconbitmap('in.ico')
    ws = root1.winfo_screenwidth()
    hs = root1.winfo_screenheight()
    w = 400
    h = 250
    x = (ws/2) - (w/2) 
    y = (hs/2) - (h/2)
    root1.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root1.resizable(width=False, height=False)
    
    new_user = user(root1)
    os.remove('in.ico')
    root1.mainloop()
    
if __name__ == "__main__" : 

    
    path = os.getcwd()
    filepath = path + '\\begin.png'
    
    change = input("你想更换背景么(y/n) : ")
    if change == 'y' :
        filename = input("请输入背景文件名(例:test.png) : ")
        filepath = path + '\\' + filename
        
    while not os.path.exists(filepath) :
        print("\n无法找到背景图片")
        filename = input("请输入背景文件名(例:test.png) : ")
        filepath = path + '\\' + filename
        
    left = img
    tmp = open('in.ico', 'wb')
    tmp.write(base64.b64decode(img))
    tmp.close()
    
    root = Tk()
    root.title("Welcome")
    root.iconbitmap('in.ico')
    os.remove('in.ico')
    
    cho_bef = tk.StringVar()
    cho_aft = tk.StringVar()
    
    im = PIL.Image.open(filepath)
    img = ImageTk.PhotoImage(im)
    lab = Label(root, image = img, font = 6, fg = 'black', width = 683, height = 384, compound = 'center').grid(row = 0)
    but = Button(root, text = 'press', command = use).grid(row = 1)

    root.mainloop()
