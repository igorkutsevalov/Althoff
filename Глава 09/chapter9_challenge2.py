answer = input("Твой любимый цвет?")
with open("fav_color.txt", "w") as f:
    f.write(answer)
