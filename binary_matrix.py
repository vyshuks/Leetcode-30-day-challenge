
class BinaryMatrix(object):

    def __init__(self, arr):
        self.arr

    def get(self, x: int, y: int) -> int:
        return self.arr[x][y]
    
    def dimensions(self) -> list[]:
        if self.arr:
            return [len(self.arr), len(self.arr[0])]

def leftMostColumnWithOne(binaryMatrix):
    rows, cols = binaryMatrix.dimensions()

    if rows==0 or cols ==0:
        return -1
    
    result = -1
    r = 0
    c = cols-1

    while r < rows and c >= 0:
        x = binaryMatrix.get(r,c)
        if x == 1:
            result = c
            c -= 1
        else:
            r += 1
    return result



