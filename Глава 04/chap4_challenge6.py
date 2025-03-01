﻿def squared(x):
    
	""" Принимает целое число и возвращает его, умножив на 2.
    
		:параметр x: целое число.
    
		:return: x умноженное на 2.
    """
    
	return x ** 2


def print_string(string):
    
	""" Выводит переданную строку.
    
		:параметр string: строка.
    """
    
	print(string)

print_string("Проверка: 1, 2, 3.")


	

def add_mult(a,b,c,x=100,z=1000):
    
	""" Возвращает результат умножения 3 обязательных параметров
	
с двумя необязательными параметрами
    
	:параметр a: целое число.
    
	:параметр b: целое число.
    
	:параметр c: целое число.
    
	:параметр x: целое число.
    
	:параметр z: целое число.
    
	:return: целое число.
    """
    
	return a + b + c * x * z


def convert(string):
    
	""" Преобразует строку в целое число.
    
	:параметр string: строка.
    
	:return: строка, преобразованная в целое число.
    """
    
	try:
        
		return float(string)
    
	except ValueError:
        
		print("Не удалось преобразовать строку в число с плавающей точкой.")