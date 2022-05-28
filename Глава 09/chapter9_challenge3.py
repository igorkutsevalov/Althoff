import csv


movies = [["Звездные войны", "Терминатор", "Искусственный интеллект"], ["Дурак", "Матильда", "Левиафан"], ["Люди в черном", "Я - робот", "Эволюция"]]

with open("movies.csv", "w") as csvfile:
    
	spamwriter = csv.writer(csvfile, delimiter=",")
    
	for movie_list in movies:
        
		spamwriter.writerow(movie_list)
