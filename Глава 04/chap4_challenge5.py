def convert(string):
    
	try:
        
		return float(string)
    
	except ValueError:
        
		print("Не удалось преобразовать строку в число с плавающей точкой.")
	

c = convert("55.0")
	
print(c)
