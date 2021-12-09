# frame.py

import tkinter
from tkinter import *
import crawling

global page
page = 0


def view():
    tk.mainloop()


def hide():
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()
    frame5.pack_forget()


def refresh():
    global page

    def click1_1():
        hide()
        frame4.pack()
        button1_1.config(text='돌아가기')
        frame4.config(text=' 지역별 신규 확진자 ')

        sub_list = list[0][2]
        c = 0
        s = 0
        for i in range(0, len(sub_list[0])):
            if c == 5:
                c = 0
                s = s + 2
            label = Label(frame4, width=9, text=sub_list[0][i], font=('', 12), borderwidth=0)
            label.grid(row=s, column=c, padx=3, pady=(6, 0))
            label = Label(frame4, width=9, text=sub_list[1][i], font=('', 12), borderwidth=0)
            label.grid(row=s + 1, column=c, padx=3, pady=(0, 3))
            c = c + 1

    if page == 0:
        hide()
        frame2.pack()
        frame3.pack()

        list = crawling.seoul()

        seoul = list[0][0]
        korea = list[0][1]

        label = Label(frame2, text=list[1][0])
        label.grid(row=0, column=0, columnspan=len(seoul[0]))
        for i in range(0, len(seoul)):
            for j in range(0, len(seoul[0])):
                if i == 0:
                    button = Button(frame2, width=6, text=seoul[i][j], font=('', 16, 'bold underline'), borderwidth=0)
                    button.grid(row=i + 1, column=j, padx=3, pady=(9, 3))
                    button.config(command=click1_1)
                else:
                    label = Label(frame2, text=seoul[i][j])
                    label.grid(row=i + 1, column=j, padx=3, pady=(3, 30))

        label = Label(frame3, text=list[1][1])
        label.grid(row=0, column=0, columnspan=len(korea[0]))
        for i in range(0, len(korea)):
            for j in range(0, len(korea[0])):
                if i == 0:
                    button = Button(frame3, width=6, text=korea[i][j], font=('', 16, 'bold underline'), borderwidth=0)
                    button.grid(row=i + 1, column=j, padx=3, pady=(9, 3))
                    if j == 3:
                        button.config(padx=46)
                else:
                    label = Label(frame3, text=korea[i][j])
                    label.grid(row=i + 1, column=j, padx=3, pady=(3, 30))


tk = Tk()
tk.title('corona')
tk.geometry('600x400')

master_frame = Frame(tk, width=600, height=400)
master_frame.pack()

frame1 = Frame(master_frame)
frame1.pack()

button1_1 = Button(frame1, width=6, text='새로고침', font=('', 10), command=refresh)
label1_1 = Label(frame1, width=42, text='뉴스제목', font=('', 12), bg='white', relief='sunken')
button1_2 = Button(frame1, width=6, text='더 보 기', font=('', 10), command='')
button1_1.grid(row=0, column=0, padx=(40, 10), pady=28)
label1_1.grid(row=0, column=1, pady=28)
button1_2.grid(row=0, column=2, padx=(10, 40), pady=28)

frame2 = LabelFrame(master_frame, text=' 서울시 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame2.pack(expand=True, pady=(0, 15))

frame3 = LabelFrame(master_frame, text=' 대한민국 코로나 발생동향 ', labelanchor='n', font=('', 12))
frame3.pack(pady=(0, 15))

frame4 = LabelFrame(master_frame, text='', labelanchor='n', font=('', 12))
frame4.pack()
frame4.pack_forget()

frame5 = Frame(master_frame, width=600, height=300, background='blue')
frame5.pack()
frame5.pack_forget()

refresh()
tk.mainloop()
