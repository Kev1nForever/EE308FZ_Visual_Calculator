import re
import tkinter.messagebox
import tkinter
import math
from math import radians

# 定义界面
window = tkinter.Tk()
window.geometry('450x500+500+200')
window.resizable(False, False)
window.title("Calculator_Kev1n")

# 定义输出文本框
contentVar = tkinter.StringVar(window, "")
contentEnter = tkinter.Entry(window, textvariable=contentVar)
contentEnter['state'] = "readonly"
contentEnter.place(x=25, y=30, width=400, height=50)
contentEnter.configure(font=('Arial', 20))
window.configure(bg="#AEEEEE")

# 定义按钮和布局
bvalue = ['(', ')', 'sin', 'cos', 'tan', 
          '7', '8', '9', '×', '^',
          '4', '5', '6', '÷', 'AC',
          '1', '2', '3', '+', 'back',
          '+/-', '0', '.', '-','=']
index = -1
for i in range(5):
    for j in range(5):
        index += 1
        if index > 25:
            break
        d = bvalue[index]
        btnB = tkinter.Button(window, text=d, command=lambda x=d: onclick(x))
        btnB.place(x=25 + j * 70, y=100 + i * 80, width=60, height=60)
        btnB.configure(font=('Arial', 20))
        btnB.configure(bg='white', fg='black')

btnB = tkinter.Button(window, text='=', command=lambda x="=": onclick(x))
btnB.place(x=305, y=420, width=60, height=60)
btnB.configure(font=('Arial', 20))
btnB.configure(bg='#FF6B81', fg='white')


# 定义运算方法
def onclick(btn):
    nop = ('+', '-', '×', '÷')
    hop = ('sin', 'cos', 'tan', '^')
    content = contentVar.get()

    if content.startswith('.'):
        content = '0' + content

    if btn in '0123456789':
        content += btn

    elif btn == 'back':
        content = content[0:-1]

    elif btn == '.':
        lastPart = re.split(r'\+|-|\*|/', content)[-1]
        if '.' in lastPart:
            tkinter.messagebox.showerror('Error ',' decimal point ')
            return
        content += btn

    elif btn == 'AC':
        content = ''

    elif btn == '(' or btn == ')':
        content += btn

    elif btn == '=':
        content = content.replace('^', '**')
        content = content.replace('÷', '/')
        content = content.replace('×', '*')
        content = str(method(content))
    
    elif btn in nop:
        
        if content.endswith(nop):
            tkinter.messagebox.showerror('Error ',' continuous operator not allowed ')
            return
        
        content += btn

    elif btn in hop:
        
        content += btn

    contentVar.set(content)


def method(result):
    if re.search(r'sin|cos|tan', result):
        result = re.sub(r'(\d+)', r'math.radians(\1)', result)
        result = result.replace("sin(", "math.sin(")
        result = result.replace("cos(", "math.cos(")
        result = result.replace("tan(", "math.tan(")
        result = str(result)
        print(result)
    try:
        x = eval(result)
    except:
       tkinter.messagebox.showerror('Error ',' expression error ')
    return format(x,'.4f')


# 运行
if __name__ == '__main__':
    window.mainloop()
