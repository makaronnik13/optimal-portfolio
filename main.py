from tkinter import ttk
import tkinter
import math
from companies import Companies
from owners import Owners

__author__ = 'makar'
from tkinter import *
c = []
o = []
root = tkinter.Tk()
s = ttk.Style()
s.theme_use('vista')
Frame = ttk.Frame(root, padding="20 20 10 10")
Frame.grid(column=0, row=0, sticky=(N, W, E, S))
E11 = ttk.Entry(Frame, width=5)
E12 = ttk.Entry(Frame, width=5)
E13 = ttk.Entry(Frame, width=5)
E14 = ttk.Entry(Frame, width=8)
E15 = ttk.Entry(Frame, width=5)
E21 = ttk.Entry(Frame, width=5)
E22 = ttk.Entry(Frame, width=5)
E23 = ttk.Entry(Frame, width=5)
E24 = ttk.Entry(Frame, width=8)
E25 = ttk.Entry(Frame, width=5)
E31 = ttk.Entry(Frame, width=5)
E32 = ttk.Entry(Frame, width=5)
E33 = ttk.Entry(Frame, width=5)
E41 = ttk.Entry(Frame, width=5)
E42 = ttk.Entry(Frame, width=5)
E43 = ttk.Entry(Frame, width=5)
A11 = ttk.Entry(Frame, width=5, state=DISABLED)
A12 = ttk.Entry(Frame, width=5, state=DISABLED)
A13 = ttk.Entry(Frame, width=5, state=DISABLED)
A14 = ttk.Entry(Frame, width=8, state=DISABLED)
A21 = ttk.Entry(Frame, width=5, state=DISABLED)
A22 = ttk.Entry(Frame, width=5, state=DISABLED)
A23 = ttk.Entry(Frame, width=5, state=DISABLED)
A24 = ttk.Entry(Frame, width=8, state=DISABLED)
A31 = ttk.Entry(Frame, width=5, state=DISABLED)
A32 = ttk.Entry(Frame, width=5, state=DISABLED)
A33 = ttk.Entry(Frame, width=5, state=DISABLED)
btn = ttk.Button(Frame, text="=>")


def hello(event):
    get_table()


def gets(Frame):
    label_per.config(text=str(round(scale1.get())) + '%')


def new_rand_table():
    for i in range(3):
        com = Companies()
        c.append(com)
    for i in range(2):
        own = Owners()
        o.append(own)
    #remake this shit{
    E11.insert(0, o[0].getval(0))
    E12.insert(0, o[0].getval(1))
    E13.insert(0, o[0].getval(2))

    E21.insert(0, o[1].getval(0))
    E22.insert(0, o[1].getval(1))
    E23.insert(0, o[1].getval(2))

    E14.insert(0, o[0].money)
    E24.insert(0, o[1].money)

    E15.insert(0, o[0].risky)
    E25.insert(0, o[1].risky)

    E31.insert(0, c[0].getval(0))
    E32.insert(0, c[1].getval(0))
    E33.insert(0, c[2].getval(0))

    E41.insert(0, c[0].getval(1))
    E42.insert(0, c[1].getval(1))
    E43.insert(0, c[2].getval(1))
    #}

def get_table():
    flag = 0
    o[0].setval(0, E11.get())
    o[0].setval(1, E12.get())
    o[0].setval(2, E13.get())
    o[1].setval(0, E21.get())
    o[1].setval(1, E22.get())
    o[1].setval(2, E23.get())
    o[0].setmoney(E14.get())
    o[1].setmoney(E24.get())
    o[0].setrisky(E15.get())
    o[1].setrisky(E25.get())
    c[0].setval(0, E31.get())
    c[0].setval(1, E41.get())
    c[1].setval(0, E32.get())
    c[1].setval(1, E42.get())
    c[2].setval(0, E33.get())
    c[2].setval(1, E43.get())
    for i in range(3):
        c[i].calc_me()
        c[i].calc_e()
        c[i].oblig_price = c[i].oblig_m
    calculate()
    A33.config(state=NORMAL)
    A32.config(state=NORMAL)
    A31.config(state=NORMAL)
    A11.config(state=NORMAL)
    A12.config(state=NORMAL)
    A13.config(state=NORMAL)
    A14.config(state=NORMAL)
    A21.config(state=NORMAL)
    A22.config(state=NORMAL)
    A23.config(state=NORMAL)
    A24.config(state=NORMAL)
    A33.delete(0, END)
    A32.delete(0, END)
    A31.delete(0, END)
    A11.delete(0, END)
    A12.delete(0, END)
    A13.delete(0, END)
    A14.delete(0, END)
    A21.delete(0, END)
    A22.delete(0, END)
    A23.delete(0, END)
    A24.delete(0, END)
    A31.insert(0, c[0].oblig_price)
    A32.insert(0, c[1].oblig_price)
    A33.insert(0, c[2].oblig_price)
    A11.insert(0, round(o[0].summ*o[0].wa*(1-o[0].w2)/c[0].oblig_price))
    A12.insert(0, round(o[0].summ*o[0].wb*(1-o[0].w2)/c[1].oblig_price))
    A13.insert(0, round(o[0].summ*o[0].wc*(1-o[0].w2)/c[2].oblig_price))
    A21.insert(0, round(o[1].summ*o[1].wa*(1-o[1].w2)/c[0].oblig_price))
    A22.insert(0, round(o[1].summ*o[1].wb*(1-o[1].w2)/c[1].oblig_price))
    A23.insert(0, round(o[1].summ*o[1].wc*(1-o[1].w2)/c[2].oblig_price))
    A14.insert(0, round(o[0].summ*o[0].w2*scale1.get()/100))
    A24.insert(0, round(o[1].summ*o[1].w2*scale1.get()/100))

    A31.config(state=DISABLED)
    A32.config(state=DISABLED)
    A33.config(state=DISABLED)
    A11.config(state=DISABLED)
    A12.config(state=DISABLED)
    A13.config(state=DISABLED)
    A14.config(state=DISABLED)
    A21.config(state=DISABLED)
    A22.config(state=DISABLED)
    A23.config(state=DISABLED)
    A24.config(state=DISABLED)

def calculate():
    Owners.calc_w(c[0].gete, c[1].gete, c[2].gete, c[0].getm, c[1].getm, c[2].getm)
    for i in range(2):
        o[i].calc_w2(scale1.get())
        o[i].calc_full(c)
        o[i].calc_sup_dem()
    balance_val()
    #пакет 1-го игрока
    print("Wbr", o[0].w2)
    print("Wa", o[0].wa*(1-o[0].w2))
    print("Wb", o[0].wb*(1-o[0].w2))
    print("Wc", o[0].wc*(1-o[0].w2))
    print(o[0].summ)

def balance_val():
    stock_sup_dem = []
    stock_summ = []
    for i in range(3):
        stock_sup_dem.append(42)
        stock_summ.append(0)
    while math.fabs(stock_sup_dem[0]) > 1 or math.fabs(stock_sup_dem[1]) > 1 or math.fabs(stock_sup_dem[2]) > 1:
        for i in range(3):
            stock_sup_dem[i] = 0
            stock_summ[i] = 0
            for j in range(2):
                stock_summ[i] += int(o[j].oblig_num[i])
                stock_sup_dem[i] += float(o[j].oblig_num[i])-int(o[j].sup_dem[i]/c[i].oblig_price)
            if stock_sup_dem[i] > 0:
                c[i].oblig_price *= 0.999
            else:
                c[i].oblig_price *= 1.001
            print(i, " ", stock_sup_dem[i], " ", c[i].oblig_price, "$")
        print("__________________________")





scale1 = ttk.Scale(Frame, orient=HORIZONTAL, from_=1, to=100, command=gets)

label_per = ttk.Label(Frame, text='0')
label_per.config(text=str(round(scale1.get())) + '%')

ttk.Label(Frame, text='держатели акций').grid(row=1, column=3, columnspan=3)
label_out = ttk.Label(Frame, text='вероятные исходы').grid(row=6, column=3, columnspan=3)
label_a = ttk.Label(Frame, text='A').grid(row=2, column=1, columnspan=1)
label_b = ttk.Label(Frame, text='B').grid(row=2, column=3, columnspan=1)
label_c = ttk.Label(Frame, text='C').grid(row=2, column=4, columnspan=1)
label_dol = ttk.Label(Frame, text='$').grid(row=2, column=17, columnspan=1)
label_a2 = ttk.Label(Frame, text='A').grid(row=2, column=14, columnspan=1)
label_b2 = ttk.Label(Frame, text='B').grid(row=2, column=15, columnspan=1)
label_c2 = ttk.Label(Frame, text='C').grid(row=2, column=16, columnspan=1)
label_dol2 = ttk.Label(Frame, text='$').grid(row=2, column=5, columnspan=1)
label_ran = ttk.Label(Frame, text='⚅').grid(row=2, column=6, columnspan=1)
label_1 = ttk.Label(Frame, text='1').grid(row=3, column=0, columnspan=1)
label_2 = ttk.Label(Frame, text='2').grid(row=4, column=0, columnspan=1)
label_12 = ttk.Label(Frame, text='1').grid(row=3, column=13, columnspan=1)
label_22 = ttk.Label(Frame, text='2').grid(row=4, column=13, columnspan=1)
label_11 = ttk.Label(Frame, text='1').grid(row=7, column=0, columnspan=1)
label_21 = ttk.Label(Frame, text='2').grid(row=8, column=0, columnspan=1)
label_opt_pac = ttk.Label(Frame, text='оптимальный пакет').grid(row=1, column=15, columnspan=3)
label_opt_val = ttk.Label(Frame, text='стоимость акций').grid(row=6, column=15, columnspan=3)

btn.bind("<Button-1>", hello)

label_per.grid(row=0, column=1, columnspan=1)
scale1.grid(row=0, column=0, columnspan=8)
new_rand_table()
#remake this shit{
E11.grid(row=3, column=1, columnspan=1)
E12.grid(row=3, column=3, columnspan=1)
E13.grid(row=3, column=4, columnspan=1)
E14.grid(row=3, column=5, columnspan=1)
E15.grid(row=3, column=6, columnspan=1)

E21.grid(row=4, column=1, columnspan=1)
E22.grid(row=4, column=3, columnspan=1)
E23.grid(row=4, column=4, columnspan=1)
E24.grid(row=4, column=5, columnspan=1)
E25.grid(row=4, column=6, columnspan=1)

E31.grid(row=7, column=1, columnspan=1)
E32.grid(row=7, column=3, columnspan=1)
E33.grid(row=7, column=4, columnspan=1)

E41.grid(row=8, column=1, columnspan=1)
E42.grid(row=8, column=3, columnspan=1)
E43.grid(row=8, column=4, columnspan=1)

btn.grid(row=4, column=12, columnspan=1)

A11.grid(row=3, column=14, columnspan=1)
A12.grid(row=3, column=15, columnspan=1)
A13.grid(row=3, column=16, columnspan=1)
A14.grid(row=3, column=17, columnspan=1)

A21.grid(row=4, column=14, columnspan=1)
A22.grid(row=4, column=15, columnspan=1)
A23.grid(row=4, column=16, columnspan=1)
A24.grid(row=4, column=17, columnspan=1)

A31.grid(row=7, column=14, columnspan=1)
A32.grid(row=7, column=15, columnspan=1)
A33.grid(row=7, column=16, columnspan=1)
#}

root.mainloop()