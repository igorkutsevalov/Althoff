class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Создано!")

or1 = Orange(10, "темный апельсин")
or1.weight = 100
or1.color = "светлый апельсин"

print(or1.weight)
print(or1.color)

