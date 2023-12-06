from math import *
from tkinter import *
root = Tk()
root.geometry("1190x520")
root.resizable(0,0)
lbl1 = Label(root, text="")
lbl2 = Label(root, text="Зміна температури, °C,")
lbl2.place_forget()
lbl3 = Label(root, text="Температурний коефіцієнт, 10^-3 K^-1,")
lbl3.place_forget()
lbl4 = Label(root, text="", font="15")
lbl4.place(x=610, y=460)
perem = IntVar()
prm = IntVar()
canvas = Canvas(root, width = 500, height = 500)
canvas.place(x=-2, y=-2)
lbl5 = Label(root, text=100)
lbl6 = Label(root, text=200)
lbl7 = Label(root, text=300)
lbl8 = Label(root, text=400)
lbl9 = Label(root, text=500)
lbl10 = Label(root, text=100)
lbl11 = Label(root, text=200)
lbl14 = Label(root, text=300)
lbl12 = Label(root, text=-273)
lbl13 = Label(root, text=0)
lbl15 = Label(root, font="1", fg="blue")
lbl16 = Label(root, font="1", fg="blue", text="Δt")
lbl17 = Label(root, font="1", fg="blue", text="α")
lbl18 = Label(root, fg="blue", font="2")
lbl18.place(x=825, y=300)
lbl19 = Label(root, text=-200)
lbl20 = Label(root, text=-100)
lbl21 = Label(root, text="R,Ом", font="1")
lbl22 = Label(root, text="t,°C", font="1")

a = None
b = None
c = None
d = None
f = None

def slct():
    if prm.get() == 1:
        canvas.delete("all")
        canvas.place_forget()
        root.geometry("690x520")
        lbl1.place(x=80-30, y=0)
        lbl2.place(x=310-30, y=0)
        lbl3.place(x=450-30, y=0)
        lbl15.place(x=235-30, y=20)
        lbl16.place(x=400-30, y=20)
        lbl17.place(x=600-30, y=20)
        lbl18.place(x=295, y=300)
        lbl15["text"] = "ρ0"
        lbl18["text"] = "ρ=ρ0(1+αΔt)"

        def startres(event):
            global a
            a = scale1.get()
            a *= 10**-8
        scale1 = Scale(root, orient=VERTICAL, length=200, from_=0, to=50, tickinterval=50, resolution=0.1)
        scale1.place(x=120-30, y=30)
        scale1.bind("<ButtonRelease-1>", startres)

        def tempcof(event):
            global c
            c = scale3.get()
            c *= 10**-3
        scale3 = Scale(root, orient=VERTICAL, length=200, from_=0, to=50, tickinterval=50, resolution=0.1)
        scale3.place(x=500-30, y=30)
        scale3.bind("<ButtonRelease-1>", tempcof)

        def calculate():
            f = c*b
            e = 1+f
            d = a*e
            d *= 10**8
            x = round(d,1)
            lbl4["text"] = "Питомий опір речовини при " + str(b) + " °C дорівнює " + str(x) + " ⋅10^-8 Ом⋅м"
            lbl4.place(x=60, y=460)

        btn = Button(root, text="Обчислити", font="34", width=12, command=calculate)
        btn.place(x=325-30, y=370)

        def select():
            scale2 = Scale(root, orient=VERTICAL, length=200, from_=0, to=360, tickinterval=50, resolution=1)
            scale2.place(x=320-30, y=30)
            def deltatemp(event):
                global b
                b = scale2.get()
                if perem.get() == 1:
                    b = b
                if perem.get() == 2:
                    b *= -1
            if perem.get() == 1:
                scale2.config(from_=0, to=300)
                lbl18["text"] = "ρ=ρ0(1+αΔt)"
            if perem.get() == 2:
                scale2.config(from_=0, to=273)
                lbl18["text"] = "ρ=ρ0(1-αΔt)"
            scale2.bind("<ButtonRelease-1>", deltatemp)

        lbl1["text"] = "Питомий опір при 0 °C, 10^-8 Ом⋅м,"
        perem1 = Radiobutton(root, text="Нагрівання ", variable=perem, value=1, bg="lightblue", fg="red", font="Arial 12", command=select)
        perem1.place(x=240-30, y=250)
        perem2 = Radiobutton(root, text="Охолодження", variable=perem, value=2, bg="lightblue", fg="blue", font="Calibri 12", command=select)
        perem2.place(x=430-30, y=250)

    if prm.get() == 2:
        lbl15["text"] = "R0"
        lbl18["text"] = "R=R0(1+αΔt)"
        lbl1.place(x=670, y=0)
        lbl2.place(x=810, y=0)
        lbl3.place(x=950, y=0)

        def startres1(event):
            global a
            a = scale1.get()
        scale1 = Scale(root, orient=VERTICAL, length=200, from_=0, to=300, tickinterval=50, resolution=1)
        scale1.place(x=680, y=30)
        scale1.bind("<ButtonRelease-1>", startres1)

        def tempcof1(event):
            global c
            c = scale3.get()
            c *= 10**-3
        scale3 = Scale(root, orient=VERTICAL, length=200, from_=0, to=50, tickinterval=50, resolution=0.1)
        scale3.place(x=1000, y=30)
        scale3.bind("<ButtonRelease-1>", tempcof1)

        def calculate():
            canvas.create_line(250, 490, 250, 0, arrow=LAST)
            canvas.create_line(0, 490, 500, 490, arrow=LAST)
            canvas.create_line(245,410,255,410)
            canvas.create_line(245,330,255,330)
            canvas.create_line(245,250,255,250)
            canvas.create_line(245,170,255,170)
            canvas.create_line(245,90,255,90)
            canvas.create_line(330,495,330,485)
            canvas.create_line(410,495,410,485)
            canvas.create_line(490,495,490,485)
            canvas.create_line(32,495,32,485)
            canvas.create_line(170, 495, 170, 485)
            canvas.create_line(50, 495, 50, 485)
            canvas.create_line(90, 495, 90, 485)
            canvas.create_line(210, 495, 210, 485)
            canvas.create_line(130, 495, 130, 485)
            canvas.create_line(290, 495, 290, 485)
            canvas.create_line(290, 495, 290, 485)
            canvas.create_line(370, 495, 370, 485)
            canvas.create_line(450, 495, 450, 485)
            canvas.create_line(245, 450, 255, 450)
            canvas.create_line(245, 370, 255, 370)
            canvas.create_line(245, 290, 255, 290)
            canvas.create_line(245, 210, 255, 210)
            canvas.create_line(245, 130, 255, 130)
            canvas.create_line(245, 50, 255, 50)
            lbl5.place(x=220, y=400)
            lbl6.place(x=220, y=320)
            lbl7.place(x=220, y=240)
            lbl8.place(x=220, y=160)
            lbl9.place(x=220, y=80)
            lbl10.place(x=315, y=493)
            lbl11.place(x=395, y=493)
            lbl14.place(x=475, y=493)
            lbl12.place(x=10, y=493)
            lbl13.place(x=242, y=493)
            lbl15.place(x=765, y=20)
            lbl16.place(x=900, y=20)
            lbl17.place(x=1100, y=20)
            lbl19.place(x=70, y=493)
            lbl20.place(x=150, y=493)
            lbl21.place(x=255, y=0)
            lbl22.place(x=495, y=460)

            f = c*b
            e = 1+f
            d = a*e
            t = d/100
            r = t*80
            q = 490-r

            i = b/100
            h = i*80
            g = 250+h

            z = a / 100
            l = z*80
            w = 490-l

            p = l*h
            s = r-l
            y = p/s

            o = h*w
            u = o/s

            canvas.create_line(250, w, g, q)
            canvas.create_line(250-h, w+w-q, 250, w)
            canvas.create_line(250-y, 490, 250-h, w+w-q)
            canvas.create_line(g, q, 250+u, 0)

            x = round(d,1)
            lbl4["text"] = "            Опір речовини при " + str(b) + " °C дорівнює " + str(x) + " Ом"
            lbl4.place(x=610, y=460)

        def clean():
            canvas.delete("all")
            lbl5.place_forget()
            lbl6.place_forget()
            lbl7.place_forget()
            lbl8.place_forget()
            lbl9.place_forget()
            lbl10.place_forget()
            lbl11.place_forget()
            lbl14.place_forget()
            lbl12.place_forget()
            lbl13.place_forget()
            lbl19.place_forget()
            lbl20.place_forget()
            lbl21.place_forget()
            lbl22.place_forget()

        btn = Button(root, text="Обчислити", font="34", width=12, command=calculate)
        btn.place(x=825-60, y=370)
        btn2 = Button(root, text="Очистити", font="34", width=12, command=clean)
        btn2.place(x=935, y=370)

        def select():
            def deltatemp1(event):
                global b
                b = scale2.get()
                if perem.get() == 1:
                    b = b
                if perem.get() == 2:
                    b *= -1
            scale2 = Scale(root, orient=VERTICAL, length=200, from_=0, to=360, tickinterval=50, resolution=1)
            scale2.place(x=820, y=30)
            scale2.bind("<ButtonRelease-1>", deltatemp1)

            if perem.get() == 1:
                scale2.config(from_=0, to=300)
                lbl18["text"] = "R=R0(1+αΔt)"
            if perem.get() == 2:
                scale2.config(from_=0, to=273)
                lbl18["text"] = "R=R0(1-αΔt)"


        lbl1["text"] = "Опір при 0 °C, Ом,"
        perem1 = Radiobutton(root, text="Нагрівання ", variable=perem, value=1, bg="lightblue", fg="red", font="Arial 12", command=select)
        perem1.place(x=740, y=250)
        perem2 = Radiobutton(root, text="Охолодження", variable=perem, value=2, bg="lightblue", fg="blue", font="Calibri 12", command=select)
        perem2.place(x=930, y=250)

prm1 = Radiobutton(root, text="Питомий опір", variable=prm, value=1, bg="lightblue", fg="red", font="Arial 12", command=slct)
prm1.place(x=735, y=250)
prm2 = Radiobutton(root, text="Опір", variable=prm, value=2, bg="lightblue", fg="blue", font="Calibri 12", command=slct)
prm2.place(x=930, y=250)

root.mainloop()