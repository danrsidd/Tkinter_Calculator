# Import tkinter module
from tkinter import *

# Create tkinter applet window
root = Tk()
root.configure(bg='#040033')
root.title('Calculator')

# Create input field to display numbers
input_box = Entry(root, width=35, borderwidth=5, bg='#080061', fg='white')
input_box.grid(row=0, column=0, columnspan=3, padx=10, pady=30)

def clear():
	'''Clears input box'''
	input_box.delete(0,END)

def button_click(num):
	'''Appends clicked number to input field'''
	current = input_box.get()
	clear()
	input_box.insert(0,str(current)+str(num))

def add():
	'''
	Stores last entered value as a global variable.
	Changes operation to addition.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'ADD'

def subtract():
	'''
	Stores last entered value as a global variable.
	Changes operation to subtraction.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'SUB'

def multiply():
	'''
	Stores last entered value as a global variable.
	Changes operation to multiplication.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'MULT'

def divide():
	'''
	Stores last entered value as a global variable.
	Changes operation to division.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'DIV'

def modulo():
	'''
	Stores last entered value as a global variable.
	Changes operation to modulo.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'MOD'

def exponent():
	'''
	Stores last entered value as a global variable.
	Changes operation to exponent.
	'''
	global value
	value = int(input_box.get())
	clear()
	global operation
	operation = 'EXP'

def equal():
	'''
	Computes specified global 'operation' on the stored values.
	'''
	global nextValue
	nextValue = int(input_box.get())
	clear()

	if operation == 'ADD':
		input_box.insert(0, value+nextValue)
	elif operation == 'SUB':
		input_box.insert(0, value-nextValue)
	elif operation == 'MULT':
		input_box.insert(0, value*nextValue)
	elif operation == 'DIV':
		input_box.insert(0, value/nextValue)
	elif operation == 'MOD':
		input_box.insert(0, value%nextValue)
	elif operation == 'EXP':
		input_box.insert(0, value**nextValue)
	else:
		pass

# Create buttons
button_1 = Button(root, text='1', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, bg='#080061', fg='white', command=lambda: button_click(0))
button_equals = Button(root, text='=', padx=87, pady=10, bg='#00c400', fg='white', command=equal)
button_mod = Button(root, text='MOD', padx=29, pady=10, bg='#e291ff', command=modulo)
button_exp = Button(root, text='^', padx=39, pady=10, bg = '#00d4cd', command=exponent)
button_add = Button(root, text='+', padx=39, pady=10, bg='#e4f005', command=add)
button_subtract = Button(root, text='-', padx=40, pady=10, bg='#ff7377', command=subtract)
button_multiply = Button(root, text='*', padx=40, pady=10, bg='#bbfad5', command=multiply)
button_divide = Button(root, text='/', padx=40, pady=10, bg='#f09a05', command=divide)
button_clear = Button(root, text='C', padx=39, pady=10, bg='red', fg='white', command=clear)

# Add buttons to grid
# Rows start at 1 because Row 0 is the input field
# Row 1
button_subtract.grid(row=1, column=0)
button_multiply.grid(row=1, column=1)
button_divide.grid(row=1, column=2)
# Row 2
button_add.grid(row=2, column=0)
button_mod.grid(row=2, column=1)
button_clear.grid(row=2, column=2)
# Row 3
button_exp.grid(row=3, column=0)
button_equals.grid(row=3, column=1, columnspan=2)
# Row 4
button_7.grid(row=4, column=0)
button_8.grid(row=4, column=1)
button_9.grid(row=4, column=2)
# Row 5
button_4.grid(row=5, column=0)
button_5.grid(row=5, column=1)
button_6.grid(row=5, column=2)
# Row 6
button_1.grid(row=6, column=0)
button_2.grid(row=6, column=1)
button_3.grid(row=6, column=2)
#Row 7
button_0.grid(row=7, column=1)

# Execute tkinter applet
root.mainloop()