numbers = [11, 32, 33, 15, 1]


while True:
    
	answer = input("Угадайте число или введите Х для выхода.")
    
	if answer == "Х":
        
		break
    
	try:
        
		answer = int(answer)
    
	except ValueError:
        
		print("пожалуйста, введите число или Х для выхода.")
    
	if answer in numbers:
        
		print("Вы угадали!")
    
	else:
        
		print("Неправильно!")
