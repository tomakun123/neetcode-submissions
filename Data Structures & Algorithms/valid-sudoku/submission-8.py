class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row check
        unique = []
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] != '.':
                    unique.append(board[row][col])
            if '.' in board[row]:
                if len(unique) != int(len(set(board[row]))-1):
                    print("row false")
                    print("row, ", board[row])
                    print("uni, ", unique)
                    return False
            else:
                if len(unique) != int(len(set(board[row]))):
                    print("row false")
                    print("row, ", board[row])
                    print("uni, ", unique)
                    return False
            unique = []
        # col check
        unique = []
        column = []
        for col in range(0,9):
            for row in range(0,9):
                column.append(board[row][col])
                if board[row][col] != '.':
                    unique.append(board[row][col])
            if '.' in column:
                if len(unique) != int(len(set(column))-1):
                    print("col false")
                    return False
            else:
                if len(unique) != int(len(set(column))):
                    print("col false")
                    return False
            column = []
            unique = []
        # sub_box check
        sub_box = []
        count = 0
        box_count = 0
        row_beg = 0
        row_end = 3
        col_beg = 0
        col_end = 3
        # get individual sub_box
        while(box_count < 9):
            for rows in range(row_beg,row_end):
                for cols in range(col_beg,col_end):
                    sub_box.append(board[rows][cols])
            col_beg += 3
            col_end += 3
            print(sub_box)

            if col_end > 9:
                row_beg += 3
                row_end += 3
                col_beg = 0
                col_end = 3

            # check dup in sub_box
            for i in range(len(sub_box)):
                if sub_box[i] == '.':
                    count += 1
            if '.' in sub_box:
                if len(set(sub_box)) != int(len(sub_box)-count+1):
                    return False
            else:
                if len(set(sub_box)) != int(len(sub_box)-count):
                    return False
            count = 0
            box_count += 1
            sub_box = []
        return True
