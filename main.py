from tkinter import*
from datetime import datetime
from random import randint
from tkinter.filedialog import*
import math

##def deff():
    
def draw(event):
    global obj,i, y, col,x, xmin, xmas, ymin, ymax,j , but, xzno, yzno, st,k, col, m
    st.append(ent.get())
    col=ent3.get()
    xmin=int(ent1.get())
    xmax=int(ent2.get())
    xzno.append(xmin)
    xzno.append(xmax)
    m=len(st)
    for i in range (11):
        obj.create_rectangle(50+i*43, 223, 50+i*43+1, 227, fill='white', outline='white' )
        obj.create_rectangle(48, 225-i*22, 52, 225-i*22,  fill='white', outline='white')
            
        
        
        
        
    n=1
    while n<len(xzno): #сортировка масива области значений х
        
        for i in range (len(xzno)-n):
            if xzno[i]>xzno[i+1]:
                xzno[i], xzno[i+1]=xzno[i+1], xzno[i]
        n=n+1
        
        
    shx=(xzno[len(xzno)-1]-xzno[0])/10 #цена деления = 43
    x=xzno[0]
    
    for i in range (11): #запись значений F(x)
        y=(eval(st[k]))
        ymas.append(round(y,1))
        xmas.append(round(x,1))
        print (ymas)
        print (xmas)
        x=x+shx
    print (st)    
    n=1
    while n<11: #сортировка y
        for i in range (11-n):
            if ymas[i]>ymas[i+1]:
                ymas[i], ymas[i+1]=ymas[i+1], ymas[i]
        n=n+1
            
    print (ymas)
        
    ymin=ymas[0]
    ymax=ymas[len(ymas)-1]
    yzno.append(ymin)
    yzno.append(ymax)

    n=1
    while n<len(yzno): #сортировка масива области значений y
        for i in range (len(yzno)-n):
            if yzno[i]>yzno[i+1]:
                yzno[i], yzno[i+1]=yzno[i+1], yzno[i]
        n=n+1
        
    ty=yzno[0]
    tx=xzno[0]
    print(yzno[len(yzno)-1],yzno[0] )
    
    shy=(yzno[len(yzno)-1]-yzno[0])/10 #цена деления = 22
    
              
    for i in range (11):
        obj.create_text(50+i*43, 235, text=str(round(tx,1)), fill='white', font=('Helvectica', '8'))
        tx=tx+shx
        obj.create_text(35, 225-i*22, text=str(round(ymas[i],1)), fill='white', font=('Helvectica', '8'))
        ty=ty+shy
    
        
        
                  
    
        
    x=xmin
    ty=ymin
    print (shy)
    print(ymin)
    print (ymax)
    for i in range (11):
        ymas[i]=round(eval(ent.get()),1)
        x=x+shx
        gy=round((ymas[i]-ymin)/shy)
        print (gy)
        obj.create_oval([50+i*43-2,225-22*gy-2], [50+i*43+2,225-22*gy+2], fill=col, outline=col)

    but['text']='Добавить'
    but.bind("<Button-1>", delt)
        

def delt(event):
    global obj,i, y, col,x, xmin, xmas, ymin, ymax,j , but,k
    
    obj.delete( "all")
    obj.create_line(50, 225, 480, 225, arrow=LAST, width=1, fill='white') ##ось Х
    obj.create_line(50, 225, 50, 5, arrow=LAST, width=1, fill='white')  ##ось Y
    obj.create_text(23, 13, text=str('F(X)'), fill='white', font=('Helvectica', '12'))
    obj.create_text(480, 210, text=str('X'), fill='white', font=('Helvectica', '12'))
    but['text']='Построить'
    
    but.bind("<Button-1>", draw)
    
ymas=[] #массивы значений
xmas=[]

xzno=[] #массивы значений осей мин и макс
yzno=[]
st=[]
x=0
k=0
root=Tk()
root.title ('Window')
root.geometry ('500x300+300+225')
obj=Canvas( width=500, height=250,bg='black')
obj.create_line(50, 225, 480, 225, arrow=LAST, width=1, fill='white') ##ось Х
obj.create_line(50, 225, 50, 5, arrow=LAST, width=1, fill='white')  ##ось Y
obj.create_text(23, 13, text=str('F(X)'), fill='white', font=('Helvectica', '12'))
obj.create_text(480, 210, text=str('X'), fill='white', font=('Helvectica', '12'))
obj.pack()


l1=Label(root, text='F(x)=',font=('Helvectica', '8')).place(x=2,y=270)
ent=Entry(root)
ent.place(x=31, y=270 ,width=100, height=20 )

l1=Label(root, text='От',font=('Helvectica', '8')).place(x=132,y=270)
ent1=Entry(root)
ent1.place(x=162, y=270 ,width=30, height=20 )
l2=Label(root, text='до',font=('Helvectica', '8')).place(x=200,y=270)
ent2=Entry(root)
ent2.place(x=230, y=270 ,width=30, height=20 )
l2=Label(root, text='- цвет',font=('Helvectica', '8')).place(x=425,y=270)
ent3=Entry(root)
ent3.place(x=350, y=270 ,width=70, height=20 )

but=Button(root, text='Построить')
but.place(x=270, y=270 ,width=70, height=20 )
but.bind("<Button-1>", draw)

root.mainloop() 
