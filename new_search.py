#-*- coding: UTF-8 -*-

import os
import base64
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import tkinter as tk
from in_ico import img

            
               
class use(Frame) :
    def __init__(self, root) :
        frame = Frame(root)
        frame.place(x = 0, y = 0, width = 600, height = 600)
        self.lab1 = Label(frame, text='文件名:')
        self.lab2 = Label(frame, text='大概位置:')
        self.lab3 = Label(frame, text = '查找结果')
        self.en1 = Entry(frame, width = 40) #文件名
        self.en2 = Entry(frame, width = 40) #大致路径
        #查找结果
        self.text = Text(frame, height = 6, width = 40)
        self.scr = Scrollbar(frame)
        self.control = False
        
        self.but1 = Button(frame, text = '查找', command = self.find)
        self.but2 = Button(frame, text = '重置', command = self.clean)
        self.but3 = Button(frame, text = '输出', command = self.output)
        self.but4 = Button(frame, text = '退出', command = root.quit)
        
        self.place()
    
    def find(self) :
        global res
        res = ''
        self.text.delete(1.0,END)
        che = self.check()
        
        if che :
            doc = self.en1.get()
            path = self.en2.get()
            search(path, doc, 1)
            self.print_text()
            
            if res == '' :
                self.text.insert(1.0, "File Not Found")
                return
            
            elif change == True :
                self.control = True
                self.text.insert(1.0, res)
                change == False
                
            self.text.insert(END, '\nFinish')
            
            
        else :
            self.text.insert(1.0, res)
            
    def print_text(self) :
        global change
        global finish
        while True :
            if change == True :
                self.control = True
                self.text.insert(1.0, res)
                change == False
            if finish == True : break
                
        
    def check(self) :
        doc = self.en1.get()
        path = self.en2.get()
        global res
        
        if path == '' :
            res = "No Path"
            return False
            
        elif os.path.isdir(path) == False :
            res = "Path Error"
            return False
        
        elif doc == '' :
            res = "No File"
            return False
            
        else :
            return True
        
    def clean(self) :
        global res
        res = ''
        
        self.en1.delete(0, END)
        self.en2.delete(0, END)
        self.text.delete(1.0, END)
    
    def output(self) :
        cont = self.text.get(1.0, END)
        error_code = ['No Path\n', 'Path Error\n', 'No File\n', 'File Not Found\n']
        if cont in error_code : return
        if cont == '\n' : return 
        
        if self.control == False : return

        path = os.getcwd()
        document = 'result.txt'
        final = os.path.join(path, document)
        
        out = open(final, 'w')
        out.write(cont)
        out.close()
        
    def place(self) :
    
        self.lab1.place(x = 20, y = 20)
        self.lab2.place(x = 20, y = 60)
        self.lab3.place(x = 20, y = 100)
        
        self.en1.place(x = 80, y = 20) #文件名
        self.en2.place(x = 80, y = 60)  #大致路径
        
        #查找结果
        self.text.place(x = 80, y = 100)
        self.scr.place(x = 364, y = 100)
        
        self.but1.place(x = 60, y = 200)
        self.but2.place(x = 140, y = 200)
        self.but3.place(x = 220, y = 200)
        self.but4.place(x = 300, y = 200)
        
        self.scr.config(command = self.text.yview)
        self.text.config(yscrollcommand = self.scr.set)
        
def search(path, doc, id_code) :
    things = os.listdir(path)
    for thing in things :
        new_path = os.path.join(path, thing)
        if doc in thing : 
            global res
            global change
            res += new_path
            res += '\n'
            change = True
            continue
        if os.path.isfile(new_path): continue
        if os.path.isdir(new_path) :
            search(new_path, doc, 0)
        
    if id_code == 1 :
        global finish
        finish = True
            
    
    

if __name__ == "__main__" :
    
    res = ''	#检索结果或错误代码
    change = False #记录实时检索结果是否发生改变
    finish = False	#记录检索是否完成
    
    #使用自定义程序框图标
    
    tmp = open('in.ico', 'wb')
    tmp.write(base64.b64decode(img))
    tmp.close()
    
    #程序框架构
    
    root = Tk()
    root.title('Search')
    root.iconbitmap('in.ico')
    os.remove('in.ico')
    
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    w = 400
    h = 250
    x = (ws/2) - (w/2) 
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.resizable(width=False, height=False)
    
    using = use(root)
    
    root.mainloop()
    

