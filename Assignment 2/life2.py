"""
This module provides functions for the 2-dimensional Game of Life.

The 2-dimensional Game of Life occurs on an n-by-n array of
cells where each cell is either alive or dead. The population of cells
evolves from one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 3
living neighbours in its 1-neighborhood (the cell itself does not
count towards the number of living neighbors).
2. Any dead cell becomes alive in the next generation if it has 3
living neighbours in its 1-neighborhood.
3. All other live cells die, and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 1-neighborhood of a cell consists of the cell itself and its
eight neighbours, which are the cells that are horizontally, vertically,
or diagonally adjacent (if those neighbors exist).

Author: Burton Ma
Date: 2021-03-06

Modified by: Dharsan Ravindran
Student number: 20219218
"""


def test_indexes(cells, row, col, func_name):
    """
    Test if row and column indexes are valid for a square array.

    This function tests if `row` and `col` are both in the
    range 0 to (n - 1), inclusive, where n is equal to
    len(cells). Raises a ValueError if an index is out of
    range.

    Parameters
    ----------
    cells : list-of-list of bool
        The n-by-n cells of a 2D Game of Life.
    row : int
        A row index for cells.
    col : int
        A column index for cells.
    func_name : str
        The name of the function that called test_indexes

    Raises
    ------
    ValueError
        If `row` or `col` is out of range.
    """
    n = len(cells)
    if row < 0:
        raise ValueError(func_name, 'number of rows < 0, row = ', row)
    elif row >= n:
        raise ValueError(func_name, 'number of rows >= len(cells), row = ', row)
    if col < 0:
        raise ValueError(func_name, 'number of cols less than zero, col = ', col)
    elif col >= n:
        raise ValueError(func_name, 'number of cols >= len(cells), col = ', col)


def make_cells(rows, cols, val):
    """
    Return an array filled with a specified value.

    Parameters
    ----------
    rows : int
        The number of rows in the array.
    cols : int
        The number of columns in the array.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list-of-lists of `rows`-by-`cols` copies of `val`

    Raises
    ------
    ValueError
        If `rows` or `cols` is less than zero.
    """
    if rows < 0:
        raise ValueError('make_cells() size less than zero, rows = ', rows)
    if cols < 0:
        raise ValueError('make_cells() size less than zero, cols = ', cols)
    a = []
    for i in range(0, rows):
        row = [val] * cols
        a.append(row)
    return a


def print_cells(cells):
    """
    Prints the representation of a 2-D array given a 2-D list.

    Prints '#' or '-' depending on the values for a certain boolean list 'cells'.
    '#' for True and '-' for false.

    Parameters
    ----------
    cells : list
        The 2-D boolean list used in to print.
    """

    for row in cells:
        for cell in row:
            if cell:
                print('#', end='')
            else:
                print('-', end='')
        print()


def neighborhood(cells, row, col):
    """
    Returns a list containing in the neighborhood of a certain cell.

    Returns a 2-D list the cells in the 1-neighborhood of in the list 'cells'
    centered around 'cells[row][col]'.

    Parameters
    ----------
    cells : list
        The larger 2-D list used to create a sublist from.
    row : int
        The first index/ row  of where the 2 neighborhood list will be built around.
    col:int
        The second index/ col  of where the 2 neighborhood list will be built around.

    Returns
    -------
    list
        A 2-D list of the 1-neighborhood cells around 'cells[row][col]' with a max area of 9 cells.

    Raises
    ------
    ValueError
        If `row` or 'col' is less than zero.
    """

    if row < 0:
        raise ValueError('neighborhood() row can not be negative index out of range row= ', str(row))
    if col < 0:
        raise ValueError('neighborhood() col can not be negative index out of range col= ', str(col))

    top_row = max(0, row - 1)
    bottom_row = min(len(cells) - 1, row + 1)
    left_column = max(0, col - 1)
    right_column = min(len(cells[row]), col + 2)
    neighbor_list = []
    if top_row == row:
        neighbor_list += [cells[top_row][left_column:right_column]]
    else:
        neighbor_list += [cells[top_row][left_column:right_column]]
        neighbor_list += [cells[row][left_column:right_column]]
    if bottom_row != row:
        neighbor_list += [cells[bottom_row][left_column:right_column]]

    return neighbor_list


def evolve(cells):
    """
     Applies the rules of the 2-dimensional Game of Life to get next generation of cells.

     Simultaneously applies the rules of the 2-dimensional Game of Life by creating
     a copy of 'cells' and changing the values based on the given rules.

    Parameters
    ----------
    cells : list
        The 2-dimensional list used in applying the game of life to.

    Raises
    ------
    ValueError
        If 'cells' is empty
    """

    if not cells:
        raise ValueError('evolve() cells can not be an empty list.')

    cells_copy = []
    for x in cells:
        sm_array = []
        for y in x:
            sm_array += [y]
        cells_copy += [sm_array]

    for index in range(len(cells)):
        for col in range(len(cells[0])):

            check = neighborhood(cells_copy, index, col)
            alive = 0

            if cells_copy[index][col]:
                for x in check:
                    for y in x:
                        if y:
                            alive += 1
                if alive == 3 or alive == 4:
                    cells[index][col] = cells[index][col]
                else:
                    cells[index][col] = not (cells[index][col])

            elif not cells_copy[index][col]:
                for x in check:
                    for y in x:
                        if y:
                            alive += 1
                if alive == 3:
                    cells[index][col] = not (cells[index][col])


def glider(cells, top_row, left_col):
    """
    Inserts the glider pattern into a list.

    Inserts a glider pattern into the list 'cells' with the pattern starting at
    'cells[top_row][left_col]'. Find 5x5 array of the glider pattern bellow:
    -----
    -#---
    --##-
    -##--
    -----

    Parameters
    ----------
    cells : list
        The 2-dimensional list used to insert the blinker pattern
    top_row : int
        The first index/row at which the glider pattern is to be inserted in the list 'cells'.
    left_col:int
        The col index/col at which the glider pattern is to be inserted in the list 'cells'.

    Raises
    ------
    ValueError
        If `top_row` or 'left_col" is less than zero or if blinker pattern does not fit into list at
        cells[top_row][left_col].
    """

    if top_row < 0:
        raise ValueError('glider() top_row can not be a negative value, top_row: ' + str(top_row))
    if left_col < 0:
        raise ValueError('glider() left_col can not be a negative value, left_col: ' + str(left_col))
    if top_row + 4 >= len(cells) or left_col + 5 > len(cells[0]):
        raise ValueError('glider() the glider pattern does not fit into the specified values.')

    cells[top_row][left_col:left_col + 5] = [False, False, False, False, False]
    cells[top_row + 1][left_col:left_col + 5] = [False, True, False, False, False]
    cells[top_row + 2][left_col:left_col + 5] = [False, False, True, True, False]
    cells[top_row + 3][left_col:left_col + 5] = [False, True, True, False, False]
    cells[top_row + 4][left_col:left_col + 5] = [False, False, False, False, False]
