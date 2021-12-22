class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_ful_profit(self, weight=30, thickness=7):
        return f"{self._length} m * {self._with} m * {weight} kgs * {thickness} cm =" \
               f" {(self._length * self._width * weight *thickness) / 1000} t"


road_1 = Road(5000,20)
print(road_1.get_ful_profit())
