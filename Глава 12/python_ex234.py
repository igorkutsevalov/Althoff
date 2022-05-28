rock = []
country = []


def collect_songs():
    song = "Укажите песню."
    ask = "Введите р (рок) или к (кантри). Введите Х для выхода"

    while True:
        genre = input(ask)
        if genre == "Х":
            break

        if genre == "р":
            rk = input(song)
            rock.append(rk)

        elif genre ==("к"):
            cy = input(song)
            country.append(cy)

        else:
            print("Неверно.")
    print(rock)
    print(country)

collect_songs()
