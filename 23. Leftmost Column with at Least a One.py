class BinaryMatrix:
    def get(self, row: int, col: int) -> int:
        pass

    def dimensions(self) -> [int, int]:
        pass


def leftMostColumnWithOne(binaryMatrix: BinaryMatrix) -> int:
    rows, cols = binaryMatrix.dimensions()
    current_row = 0
    current_col = cols - 1
    leftmost_col = -1

    while current_row < rows and current_col >= 0:
        if binaryMatrix.get(current_row, current_col) == 1:
            leftmost_col = current_col
            current_col -= 1  # move left
        else:
            current_row += 1  # move down

    return leftmost_col

# Example Usage:
# Assuming BinaryMatrix is properly implemented
# binaryMatrix = BinaryMatrix()
# print(leftMostColumnWithOne(binaryMatrix))
