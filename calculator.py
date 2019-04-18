from tkinter import *
def task(num):
    global operator
    operator= operator + str(num)
    text_input.set(operator)

def equal():
    try:
        global operator
        result=str(eval(operator))
        text_input.set(result)
        operator=''
    except:
        text_input.set('error')
        operator=''

def clear():
    global operator
    operator=''
    text_input.set('')


cal= Tk()
cal.title('calculator')
operator=''
text_input= StringVar()
textDisplay= Entry(cal,font=('arial', 23 ,'bold'), textvariable=text_input,bd=30,insertwidth=4, bg='powder blue',justify='right').grid(columnspan=4)
btnclear=Button(cal, padx=16,bd=7,text='C',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=clear).grid(row=1,column=0)
btndiv=Button(cal, padx=16,bd=7,text='%',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('%')).grid(row=1,column=1)
btnmul=Button(cal, padx=16,bd=7,text='X',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('*')).grid(row=1,column=2)
btnAdd=Button(cal, padx=16,bd=7,text='+',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('+')).grid(row=1,column=3)
# ------------------------first row------------------------

btn1=Button(cal, padx=16,bd=7,text='1',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(1)).grid(row=2,column=0)
btn2=Button(cal, padx=16,bd=7,text='2',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(2)).grid(row=2,column=1)
btn3=Button(cal, padx=16,bd=7,text='3',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(3)).grid(row=2,column=2)
btnSub=Button(cal, padx=16,bd=7,text='-',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('-')).grid(row=2,column=3)


# ------------------------second row-----------
btn4=Button(cal, padx=16,bd=7,text='4',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(4)).grid(row=3,column=0)
btn5=Button(cal, padx=16,bd=7,text='5',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(5)).grid(row=3,column=1)
btn6=Button(cal, padx=16,bd=7,text='6',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(6)).grid(row=3,column=2)
btnequal=Button(cal, padx=16,bd=7,text='=',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=equal).grid(row=3,column=3)

# =========================third row--------------------------

btn0=Button(cal, padx=16,bd=7,text='0',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('0')).grid(row=4,column=3)
btn7=Button(cal, padx=16,bd=7,text='7',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task('7')).grid(row=4,column=0)
btn8=Button(cal, padx=16,bd=7,text='8',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(8)).grid(row=4,column=1)
btn9=Button(cal, padx=16,bd=7,text='9',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2, width=3,command=lambda:task(9)).grid(row=4,column=2)
# -------------------------------fourth row======================================

# btnEquals=Button(cal, padx=12,bd=5,text='=',fg='black',font=('arial',14,'bold'),bg='powder blue', height=2,command=equal().grid(row=4,column=0)





cal.mainloop()
