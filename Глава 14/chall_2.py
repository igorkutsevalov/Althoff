class Shape():

    def what_am_i(self):

        print("Я - фигура.")




class Square(Shape):

    square_list = []



    def __init__(self, s1):

        self.s1 = s1

        self.square_list.append(self)



    def calculate_perimeter(self):

        return self.s1 * 4



    def what_am_i(self):

        super().what_am_i()

        print("Я - фигура.")



    def __repr__(self):

        return "{} на {} на {} на {}".format(self.s1, self.s1, self.s1, self.s1)



a_square = Square(29)

print(a_square)
