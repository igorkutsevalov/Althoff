import csv


with open("st.csv", "w", newline='') as f:
    write = csv.writer(f, delimiter=",")
    write.writerow(["один",
                    "два",
                    "три"])
    write.writerow(["четыре",
                    "пять",
                    "шесть"])
