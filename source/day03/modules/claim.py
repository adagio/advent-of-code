from dataclasses import dataclass

@dataclass
class DataClassClaim:
    __slots__ = ['id', 'left_edge', 'top_edge', 'width', 'height']
    id: int
    left_edge: int
    top_edge: int
    width: int
    height: int

    def __str__(self):
        return f'#{self.id} @ {self.left_edge},{self.top_edge}: {self.width}x{self.height}'

    def get_coords(self):
        coords = []
        for i in range(0, self.width):
            for j in range(0, self.height):
                coord = (i + self.left_edge, j + self.top_edge)
                coords.append(coord)
        return coords
