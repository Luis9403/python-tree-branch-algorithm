from xyz import Point, Vector


class Line():

    @classmethod
    def create_bound(self, start_point: Point, end_point: Point) -> None:
        self.start_point = start_point
        self.end_point = end_point
        self.direction = start_point

    @property
    def start_point(self):
        return self.start_point

    @property
    def end_point(self):
        return self.end_point

    @property
    def direction(self) -> Vector:

        return self.direction
