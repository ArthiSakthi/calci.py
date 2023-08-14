from tkinter import *
win=Tk()
win.geometry("300x350")
win.title(" GUI Calculator")
def btn_click(num):
    global expression
    expression=expression + str(num)
    input_text.set(expression)
def bt_clear(): 
    global expression 
    expression= "" 
    input_text.set("")
def bt_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
expression=""
input_text =StringVar()
input_frame=Frame(win, width=50, height=5, highlightbackground="blue", highlightcolor="black", highlightthickness=2) 
input_frame.pack() 
input_field=Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="white", justify=LEFT) 
input_field.pack()
btns_frame=Frame(win, width=312, height=272, bg="blue")
btns_frame.pack() 
clear=Button(btns_frame, text = "C", fg = "black", width = 32, height = 3, bg = "white", command = lambda: bt_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
divide=Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bg = "skyblue", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
#first row 
seven=Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bg = "white", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
eight=Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bg = "white", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
nine=Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bg = "white",command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1) 
multiply=Button(btns_frame, text = "*", fg = "black", width = 10, height = 3,bg = "skyblue", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
#second row
four=Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bg = "white", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1) 
five=Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bg = "white", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six=Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bg = "white", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus=Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bg = "skyblue",command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
#third row
one=Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bg = "white",command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1) 
two=Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bg = "white",command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three=Button(btns_frame, text = "3", fg = "black", width = 10, height = 3,bg = "white",command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus=Button(btns_frame, text = "+", fg = "black", width = 10, height = 3,bg = "skyblue",command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
# fourth row 
zero=Button(btns_frame, text = "0", fg = "black", width = 21, height = 3,bg = "white",command = lambda: btn_click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1) 
point=Button(btns_frame, text = ".", fg = "black", width = 10, height = 3,bg = "skyblue",command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1) 
equal=Button(btns_frame, text = "=", fg = "black", width = 10, height = 3,bg = "skyblue",command = lambda: bt_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
win.mainloop()
