@[TOC](Visual Calculator Based on Python)
# I. Introduction
>This blog is for EE308FZ to show the implementation of the Visual calculator including the function of addition, subtraction, multiplication, division, clearing, exponentiation and trigonometric function.

| The Link Your Class  | 	https://bbs.csdn.net/forums/ssynkqtd-04 |
|--|--|
| The Link of Requirement of This Assignment |https://bbs.csdn.net/topics/617332156  |
| The Aim of This Assignment |Visual 	Calculator |
| MU STU ID and FZU STU ID  | 21124868（MU）/832101102(FZU) |

 **Link to the finished project code**：
# II. Project Work

## PSP Form
| **Personal Software Process Stages**    | Estimated Time（minutes） | Actual Time（minutes） |
| :-------------------------------------- | :------------------------ | :--------------------- |
| **Planning**                                |  **50**                         |        **60**                |
| • Estimate                              |                50           |     60                   |
| **Development**                             |           **325**              |       **385**                |
| • Analysis                              |               25            |              30          |
| • Design Spec                           |               20            |              15          |
| • Design Review                         |                 10          |               15         |
| • Coding Standard                       |                    10       |               10         |
| • Design                                |                   60        |                70        |
| • Coding                                |                     100      |                 120       |
| • Code Review                           |            60              |                 75       |
| • Test                                  |                     40      |                 50       |
| **Reporting**                               |             **100**              |   **115**                     |
| • Test Report                            |                 60          |           65             |
| • Size Measurement                      |             10              |       10                 |
| • Postmortem & Process Improvement Plan |                  30         |         40               |
| **Sum**                                 |             **475**              |        **560**                |




## Description of problem-solving ideas
### 1. How I think about the question
In this project, the basic goal is to complete the functions including input numbers and addition, subtraction, multiplication, division, subtraction, and then implement the functions including trigonometric functions and power functions.

 **Python** is very easy and concise for creating visual tasks, so it can be used to accomplish this task.
 
### 2. Find Information
After reading and learning related materials on CSDN, Bilibili, Github, I found that  **tkinter** can be used to build visual interfaces, and it is extremely easy to use.

## Design and Implementation process
The design of the calculator is divided into several parts：
- **Visual Interface**
- **Interactive button logic**
- **Calculation logic**
### Visual Interface：
For this problem, **tkinter** can help us directly implement the initialization and design of the interface.

```python
# Define interface
window = tkinter.Tk()
window.geometry('450x500+500+200')
window.resizable(False, False)
window.title("Calculator_Kev1n")

# Defines the output text box
contentVar = tkinter.StringVar(window, "")
contentEnter = tkinter.Entry(window, textvariable=contentVar)
contentEnter['state'] = "readonly"
contentEnter.place(x=25, y=30, width=400, height=50)
contentEnter.configure(font=('Arial', 20))
window.configure(bg="#AEEEEE")
```

The initialization of the interface is shown in the figure below. We can adjust the font, interface size and color.
### Interactive button logic
The buttons on the calculator need to be interactive and correctly displayed on the screen, we directly use the Button function in tkinter (onclick). Display results and calculations are controlled by setting different outputs when different buttons are pressed.
It should be noted that when we press '=', the calculation result needs to be obtained directly and displayed in the output box, so '=' is the key to end an operation, and if there is a problem with the calculation logic, error should be displayed.

### Calculation logic
After writing a lot of computational logic code by hand, I found that the **eval ()** function is a good way to implement the function of computation without a lot of independent code and can greatly simplify the code. But there are a few things to note：
 1. Clicks a number button(for example:1, 2, 3): Add the corresponding number to the end of the input box.
 2. Clicks the operator button:
- Four-rule operation(+,-,×,÷)： Note that the user should see **×** and **÷** on the interface, but should use * and / when programming the calculation. Therefore, after clicking the multiply and divide button, it is necessary to make the corresponding replacement before calculation
- Trigonometric operation(sin,cos,tan): In eval() calculations, it does not directly recognize trigonometric functions such as sin(), which need to be replaced with math.sin(), and when using the calculator, the user is used to inputting an angle, while eval() calculates radians, so it is necessary to convert the angle inputted by the user into radians and then carry out calculations.

3. Incorrect formula entered： We must give feedback and ideally point out the cause of the error.

 ![在这里插入图片描述](https://img-blog.csdnimg.cn/3a6b5d76a19e41fcbf6da005755a1cb1.png#pic_center)

## Code Description
### A. Appearance and Layout
For the construction of the window, we use tkinter, as described above:

```python
# Define interface
window = tkinter.Tk()
window.geometry('450x500+500+200')
window.resizable(False, False)
window.title("Calculator_Kev1n")

# Defines the output text box
contentVar = tkinter.StringVar(window, "")
contentEnter = tkinter.Entry(window, textvariable=contentVar)
contentEnter['state'] = "readonly"
contentEnter.place(x=25, y=30, width=400, height=50)
contentEnter.configure(font=('Arial', 20))
window.configure(bg="#AEEEEE")

```
We use a circular approach to set the key and its size and color, reducing code redundancy.
The code design of the key layout is as follows:
```python

# Define the buttons and layout
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
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/67c1b08332ac45a68051e17adfc6cc9f.png#pic_center)

### B. Operation Method
By defining the onclick function with different settings for different key clicks, it displays the formula and calculates it when '=' is clicked.

```python
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
```
It also defines the function that performs the calculations, categorizes the error cases, and replaces the correct operation symbols before the calculation.

```python
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
```
# III. Result Displaying
![在这里插入图片描述](https://img-blog.csdnimg.cn/3e04cffd2ec2499d951595f25d19ad5b.gif#pic_center)
The finished product, as shown in the figure, can normally realize the functions of addition, subtraction, multiplication and division, trigonometric functions, power functions and so on.
# IV. Summary
This calculator project enabled me to learn a lot about project implementation, including pre-project task analysis, functional planning, development, testing, optimization and modification, and improved my ability to collect information and independent learning, as well as how to optimize the product and consider user habits. At the same time, I have learned a lot of programming knowledge about visualization, and also learned to use GitHub for code version control and development. I will continue to learn about software engineering and hope to make progress.
