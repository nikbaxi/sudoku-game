import copy

class suduko:
    def __init__(self):
        self.sudoku =  [
                            [0, 7, 0, 8, 9, 0, 0, 0, 0 ],
                            [0, 5, 0, 0, 0, 0, 3, 0, 4 ],
                            [0, 2, 0, 0, 4, 0, 0, 1, 0 ],
                            [5, 6, 8, 9, 0, 0, 4, 7, 2 ],
                            [0, 0, 0, 6, 0, 0, 0, 0, 0 ],
                            [1, 0, 7, 0, 5, 0, 6, 3, 8 ],
                            [7, 3, 0, 1, 0, 2, 0, 8, 0 ],
                            [6, 0, 0, 4, 7, 0, 1, 0, 0 ],
                            [2, 0, 9, 0, 3, 8, 7, 0, 6 ]
                        ]

    def get_original_sudoku(self):
        return self.sudoku
    
    def get_deep_copy_sudoku(self):
        return copy.deepcopy(self.sudoku)


def fixed_digit_in_row(original_sudoku, row):    #gives us the column no. for the fixed digits in the table
    fixed_columns = []
    for i in range(0,9):
        if original_sudoku[row][i] != 0:
            fixed_columns.append(i)
    return fixed_columns

def row_duplicates(sudoku, row, digit):
    for i in range(0,9):
        if sudoku[row][i] == digit:
            print("found in row")
            return True
    return False

def col_duplicates(sudoku, col, digit):
    for i in range(0,9):
        if sudoku[i][col] == digit:
            print("found in col", i, col)
            return True
    return False

def box_duplicates(sudoku, box, digit):
    for i in range(0,9):
        if sudoku[box][i] == digit:
            print("found in box", box, i)
            # print(sudoku)
            return True
    return False

def convert_sudoku_to_boxes(cs):
    
    boxes = [
        [cs[0][0], cs[0][1], cs[0][2], cs[1][0], cs[1][1], cs[1][2], cs[2][0], cs[2][1], cs[2][2]],
        [cs[0][3], cs[0][4], cs[0][5], cs[1][3], cs[1][4], cs[1][5], cs[2][3], cs[2][4], cs[2][5]],
        [cs[0][6], cs[0][7], cs[0][8], cs[1][6], cs[1][7], cs[1][8], cs[2][6], cs[2][7], cs[2][8]],
        [cs[3][0], cs[3][1], cs[3][2], cs[4][0], cs[4][1], cs[4][2], cs[5][0], cs[5][1], cs[5][2]],
        [cs[3][3], cs[3][4], cs[3][5], cs[4][3], cs[4][4], cs[4][5], cs[5][3], cs[5][4], cs[5][5]],
        [cs[3][6], cs[3][7], cs[3][8], cs[4][6], cs[4][7], cs[4][8], cs[5][6], cs[5][7], cs[5][8]],
        [cs[6][0], cs[6][1], cs[6][2], cs[7][0], cs[7][1], cs[7][2], cs[8][0], cs[8][1], cs[8][2]],
        [cs[6][3], cs[6][4], cs[6][5], cs[7][3], cs[7][4], cs[7][5], cs[8][3], cs[8][4], cs[8][5]],
        [cs[6][6], cs[6][7], cs[6][8], cs[7][6], cs[7][7], cs[7][8], cs[8][6], cs[8][7], cs[8][8]]
    ]

    return boxes 

def which_box(row, col):
    box = 0
    if row < 3:
        if col < 3:
            box = 0
        elif col > 2 and col < 6:
            box = 1
        elif col > 5 and col < 9:
            box = 2
    elif row > 2 and row < 6:
        if col < 3:
            box = 3
        elif col > 2 and col < 6:
            box = 4
        elif col > 5 and col < 9:
            box = 5
    elif row > 5 and row < 9:
        if col < 3:
            box = 6
        elif col > 2 and col < 6:
            box = 7
        elif col > 5 and col < 9:
            box = 8
    
    return box 

def add_digit(original_sudoku, sudoku, row, col, data=None):
    digits = []
    for i in range(1,10):
        # print(i, "digit")
        if data != i:
            digits.append(i)

    if data == None or data == 0:
        for i in range(1, 10):
            if check_duplicates(suduko, row, col, i):
                sudoku[row][col] = i
                return sudoku[row][col]
        print("count find a digit for", row, col)
        sudoku[row][col] = 0
    
    return sudoku[row][col]


def update_row_to_match(original_sudoku, sudoku, row):
    # check if the row contains 0
    copied_row = sudoku[row]
    print(copied_row)

    if 0 in copied_row:
        #get fixed column in the row
        fixed_column = fixed_digit_in_row(original_sudoku, row)
        print('fixed_column:', fixed_column)
        
        missing_digit = 0
        for i in range(1, 10):
            if i not in copied_row:
                missing_digit = i
        
        col_of_missing_digit = 0
        for i in range(0,9):
            if copied_row[i] == 0:
                col_of_missing_digit = i

        print(missing_digit, col_of_missing_digit)
        for i in range(0, 9):
            if i not in fixed_column:
                print(i)
                import pdb; pdb.set_trace()
                col = i
                if check_duplicates(sudoku, row, col, missing_digit):
                    tmp = sudoku[row][col]
                    if check_duplicates(sudoku, row, col_of_missing_digit, tmp):
                        print("yes")
                        sudoku[row][col] = missing_digit

    return sudoku

def check_duplicates(suduko, row, col, digit):
    if not row_duplicates(sudoku, row, digit):
        if not col_duplicates(sudoku, col, digit):
            boxes = convert_sudoku_to_boxes(sudoku)
            box = which_box(row, col)
            if not box_duplicates(boxes, box, digit):
                return True
    
    return False

def check_for_valid_digits(sudoku, copy_sudoku, row, col):
    digits_array = []
    for i in range(1, 10):
        if not row_duplicates(sudoku, row, i):
            if not col_duplicates(sudoku, col, i):
                boxes = convert_sudoku_to_boxes(sudoku)
                box = which_box(row, col)
                if not box_duplicates(boxes, box, i):
                    digits_array.append(i)
    return digits_array
                    


if __name__ == "__main__":

    # sudoku
    sudoku = suduko()
    os = sudoku.get_original_sudoku()
    cs = sudoku.get_deep_copy_sudoku()

    flag = True

    #1> fid the no. of fixed digits in each box

    fixed_digits = {}
    length_of_each_box = {}
    for i in range(0,9):
        for j in range(0,9):
            if cs[i][j] != 0:
                #find which box
                box = which_box(i, j)
                box_name = 'box' + str(box)
                if box_name not in fixed_digits:
                    fixed_digits[box_name] = []
                fixed_digits[box_name].append(cs[i][j])
    
    # find the box with higest no of fixed digits
    box_to_select = [ [], [], [], [], [], [], [], [], [], [] ]
    for key, value in fixed_digits.items():
        print(key, value)
        length_of_each_box[key] = value.__len__()

        box_to_select[value.__len__()].append(key)
    print(length_of_each_box)
    print(box_to_select)

    #selecting the first box
    for i in range(9,-1,-1):
        if box_to_select[i] != []:
            print(box_to_select[i])
            for box in box_to_select[i]:
                print(box)
                for row in range(0,9):
                    for col in range(0,9):
                        if box.endswith(str(which_box(row, col))):
                            if cs[row][col] == 0:
                                cs[row][col] = check_for_valid_digits(os, cs, row, col)
                                if cs[row][col].__len__() == 1:
                                    cs[row][col] = cs[row][col][0]
                                    os[row][col] = cs[row][col]

    print(cs)
    print(os)
    
    count = {
            'box1': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box2': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box3': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box4': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box5': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box6': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box7': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box8': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
            'box9': { 1:0 ,2:0 ,3:0 , 4:0, 5:0, 6:0, 7:0, 8:0, 9:0 },
        }
    boxes = convert_sudoku_to_boxes(cs)
    #time to apply the sets 
    for i in range(0,9):
        for j in range(0,9):
            if isinstance(boxes[i][j], (list)):
                
                # import pdb; pdb.set_trace()
                box_name = "box" + str(i+1)
                for k in boxes[i][j]:
                    if k in count[box_name]:
                        count[box_name][k] = count[box_name][k] + 1
    
    print(count)
    
                        

