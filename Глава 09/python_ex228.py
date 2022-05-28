import csv


# убедитесь,  что этот файл
# создается из предыдущего примера


with open("st.csv", "r") as f:
    r = csv.reader(f, delimiter=",")
    for row in r:
        print(",".join(row))
