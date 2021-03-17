from os import system, name
import math
import time


val = ('0.00')
r1 = [' . ',' 1 ',' 2 ',' 3 ',' 4 ',' 5 ',' 6 ',' 7 ',
		' 8 ',' 9 ',' 0 ',' - ',' = ','   ','   ','   ']
r2 = ['INV','^.5','x^2','x^y',' x!','E10','log',' ln',
		' pi', ' + ', ' * ',' / ','clr','   ','   ','   ']
r3 = ['.','1','2','3','4','5','6','7','8','9','0','-']
r4 = ['+','-','*','/']



def display_board(val):
	print('',"-"*89)
	print('|','     '*17,'  |\n|',end='')
	#print('|','     '*17,'  |')
	print((' '*69),f'{val:>19}|')
	print('|','     '*17,'  |')
	print('',"-"*89)
	print(('|     '*15)+'|','')
	print('|',r1[0],'|',r1[1],'|',r1[2],'|',r1[3],'|',r1[4],'|',
			r1[5],'|',r1[6],'|',r1[7],'|',r1[8],'|',r1[9],'|',r1[10],
			'|',r1[11],'|',r1[12],'|',r1[13],'|',r1[14],'|')
	print(('|     '*15)+'|','')
	print('',"-"*98)
	print('        ',('|     '*15)+'|','')
	print('        ','|',r2[0],'|',r2[1],'|',r2[2],'|',r2[3],'|',r2[4],
			'|',r2[5],'|',r2[6],'|',r2[7],'|',r2[8],'|',r2[9],'|',r2[10],
				'|',r2[11],'|',r2[12],'|',r2[13],'|',r2[14],'|')
	print('        ',('|     '*15)+'|','')
	print('         ',"-"*89)

def clear():
	"""call windows to clear the console"""
	if name == 'nt':
		_=system('cls')

def get_input():
	"""get raw input from the user"""
	return input(' ')

def check_val_numeric(val):
	"""returns True if val is numeric"""
	try:
		if val[0] in r3:
			return True
		else:
			return False
	except TypeError:
		pass

def check_val_int(val):
	"""returns True if val is integer"""
	return isinstance(val, int)

def add(val,new_val):
	"""return sum"""
	return val + new_val

def sub(val, new_val):
	"""return difference"""
	return val - new_val

def mult(val, new_val):
	"""return product"""
	return val * new_val

def div(val, new_val):
	"""return quotient"""
	try:
		return val / new_val
	except ZeroDivisionError:
		return 'Math Error'

def check_equal(operator):
	"""returns True if operator is '=' """
	if operator == "=":
		return True
def return_pi():
	"""returns pi when called"""
	return math.pi

def calc_ln(val):
	"""calculates the natural log of a given value"""
	try:
		return math.log(val)
	except ValueError:
		return "Math Error"

def calc_log(val):
	"""calculates the log base 10 of a given value"""
	try:
		return math.log10(val)
	except ValueError:
		return "Math Error"

def calc_E10(val):
	"""calculates a value times given power of 10""" 
	power = int(input("Enter the power of 10: "))
	return val*10**power

def calc_factorial(val):
	"""calculates the factorial of an integer"""
	try:
		return math.factorial(val)
	except ValueError:
		return "Math Error"

def calc_power(val):
	"""calculates the value to a given power"""
	power = int(input("Enter the power of 10: "))
	return val**power
	 
def calc_square(val):
	"""squares a given value"""
	return val**2

def calc_square_root(val):
	"""squares a given value"""
	return val**(0.5)

def calc_inverse(val):
	"""returns the inverse of a value"""
	return val**(-1)

if __name__=='__main__':
	running = True
	backslash = chr(92)
	while running == True:
		clear()
		val = ('0.00')
		display_board(val)
		val = get_input()
		if val == 'clr': 
			clear()
			continue
		if val == backslash:
			clear()
			continue  
		clear()
		if val == 'pi' or val == 'o':
			val = return_pi()
		display_board(val)
		if check_val_numeric(val):
			if check_val_int(val):
				val = int(val)
			else:
				val = float(val)

		while running == True:
			operator = get_input()
			clear()
			display_board(operator)
			
			if operator == 'ln' or operator == 'i':
				clear()
				val = calc_ln(val)
				if val == 'Math Error':
					display_board(val)
					time.sleep(2)
					break
				display_board(val)
				continue
			
			if operator == 'log' or operator == 'u':
				clear()
				val = calc_log(val)
				if val == 'Math Error':
					display_board(val)
					time.sleep(2)
					break
				display_board(val)
				continue	
			
			if operator == 'E10' or operator == 'y':
				clear()
				val = calc_E10(val)
				display_board(val)
				continue

			if operator == 'x!' or operator == 't':
				clear()	
				
				val = calc_factorial(val)
				if val == 'Math Error':
					display_board(val)
					time.sleep(2)
					break
				display_board(val)
				continue

			if operator == 'x^y' or operator == 'r':
				clear()	
				val = calc_power(val)
				display_board(val)
				continue
			
			if operator == 'x^2' or operator == 'e':
				clear()
				val = calc_square(val)
				display_board(val)
				continue

			if operator == '^.5' or operator == 'w':
				clear()
				val = calc_square_root(val)
				display_board(val)
				continue

			if operator == 'INV' or operator == 'q':
				clear()
				val = calc_inverse(val)
				display_board(val)
				continue		

			
			if operator == 'clr': 
				clear()
				break
			if operator == backslash:
				clear()
				break
			

			
			if check_equal(operator):
				clear()
				display_board(final_val)
				break
			new_val = get_input()
			if new_val == 'clr': 
				clear()
				break
			if new_val == backslash:
				clear()
				break
			if new_val == 'pi' or new_val == 'o':
				new_val = return_pi()
			if check_val_numeric(new_val):
				if check_val_int(new_val):
					new_val = int(new_val)
				else:
					new_val = float(new_val)
			clear()
			display_board(new_val)
			if new_val == 'o':
				new_val = math.pi
			operator_dict = {'+':add(val,new_val), '-': sub(val, new_val),
				 '*':mult(val,new_val), '/': div(val,new_val), 
				 'p':add(val,new_val), '[':mult(val,new_val),
				  ']':div(val,new_val)}
			final_val = operator_dict.get(operator)
			
			clear()
			display_board(final_val)
			if final_val == 'Math Error':
				break
			val = final_val



	
	#pass

x=input()
