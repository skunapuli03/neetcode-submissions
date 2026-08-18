class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # I need one set for each row, column, and 3x3 box.
        # Each set stores numbers I have already seen there.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Look at every square on the board.
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                # A dot is an empty square, so it cannot create a duplicate.
                if value == ".":
                    continue

                # Figure out which of the 9 small 3x3 boxes this cell belongs to.
                # Example: row 4, column 7 belongs to box (1, 2).
                box_index = (r // 3) * 3 + (c // 3)

                # If this number already appeared in its row, column, or box,
                # the board is not valid.
                if (
                    value in rows[r]
                    or value in cols[c]
                    or value in boxes[box_index]
                ):
                    return False

                # I have not seen it yet, so remember it in all three places.
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        # I checked every filled square and found no duplicate.
        return True