class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.height + 2 * self.width

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        s = ""
        for h in range(self.height):
            s = s + "*" * self.width + "\n"
        return s

    def get_amount_inside(self, shape):
        result = self.width / shape.width * self.height / shape.height
        return int(result)

    def __repr__(self):
        return 'Rectangle(width={0.width!r}, height={0.height!r})'.format(self)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, side):
        self.__init__(side)

    def set_width(self, width):
        self.__init__(width)

    def set_height(self, height):
        self.__init__(height)

    def __repr__(self):
        return 'Square(side={0.side!r})'.format(self)
