me = {
"вес": "60",
"люб_цвет": "красный",
 "люб_автор": "Пелевин"
}


answer = input("Укажите вес, люб_цвет или люб_автор")

if answer in me:
    
	result = me[answer]
    
	print(result)
