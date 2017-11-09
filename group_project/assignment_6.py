# Example. Use it as a base to build your own template.
BOARD_TEMPLATE = """
0  |  O  |  X
--------------
X  |  X  |  O
--------------
0  |  X  |  O
"""


def format_tic_tac_toe_board(first_row, second_row, third_row):
    row_line = '--------------'

    str_line = "\n{}  |  {}  |  {}\n{}\n{}  |  {}  |  {}\n{}\n{}  |  {}  |  {}\n".format\
                (first_row[0], first_row[1], first_row[2], row_line, 
                second_row[0], second_row[1], second_row[2], row_line, 
                third_row[0], third_row[1], third_row[2], row_line)
    
    return str_line#
    

def test_format_board():
    """
    This is the board used in this test:

        X  |  O  |  X
        --------------
        O  |  X  |  O
        --------------
        O  |  O  |  X

    """
    first_row = 'XOX'
    second_row = 'OXO'
    third_row = 'OOX'
    
    expected_board = """
X  |  O  |  X
--------------
O  |  X  |  O
--------------
O  |  O  |  X
"""
    board = format_tic_tac_toe_board(first_row, second_row, third_row)

    assert board == expected_board
