"""
This module provides functions for the -dimensional Game of Life.

The 1-dimensional Game of Life occurs on a list of cells where each
cell is either alive or dead. The population of cells evolves from
one generation to the next according to three rules:

1. Any live cell survives into the next generation if it has 2 or 4
living neighbours in its 2-neighborhood.
2. Any dead cell becomes alive in the next generation if it has 2 or 3
living neighbours in its 2-neighborhood.
3. All other live cells die and all other dead cells remain dead.

The rules are applied to each cell simultaneously to compute the
next generation of cells.

The 2-neighborhood of a cell consists of the cell itself and its
two neighbors to the left and two neighbors to the right of the cell
(if those neighbors exist).

Author: Burton Ma
Date: 2021-03-06

Modified by: Dharsan Ravindran
Student number: 20219218
"""


def make_cells(n, val):
    """
    Return a list filled with a specified value.

    Uses the integer 'n' to determine the length of the list and returns a list
    with 'n' copies of 'val'.

    Parameters
    ----------
    n : int
        The number of elements in the returned list.
    val : bool
        The element to appear repeatedly in the returned list.

    Returns
    -------
    list
        A list of `n` copies of `val`

    Raises
    ------
    ValueError
        If `n` is less than zero.
    """

    if n < 0:
        raise ValueError('make_cells() number of elements less than zero, n = ' + str(n))
    a = [val] * n
    return a


def print_cells(cells):
    """
    Prints the representation of a 1-D array given a 1-D list.

    Prints '#' or '-' depending on the values for a certain boolean list 'cells'.
    '#' for True and '-' for false.

    Parameters
    ----------
    cells : list
        The boolean list used in to print.
    """

    for cell in cells:
        if cell:
            print('#', end='')
        else:
            print('-', end='')
    print()


def neighborhood(cells, index):
    """
    Returns a list containing in the neighborhood of a certain cell.

    Returns a list the cells in the 2-neighborhood of in the list 'cells'
    centered around the index of 'index'.

    Parameters
    ----------
    cells : list
        The larger list used to create a sublist from.
    index : int
        The index of where the 2 neighborhood list will be built around.

    Returns
    -------
    list
        A list of the 2-neighborhood cells around 'index' with a max length of 5.

    Raises
    ------
    ValueError
        If `index` is less than zero.
    """

    if index < 0:
        raise ValueError("neighbourhood() index can not be a negative value, index = ", str(index))

    left_index = index - 2
    right_index = index + 3
    if left_index < 0:
        left_index = 0
    if right_index > len(cells):
        right_index = len(cells)
    return cells[left_index:right_index]


def evolve(cells):
    """
     Applies the rules of the 1-dimensional Game of Life.

     Simultaneously applies the rules of the 1-dimensional Game of Life by creating
     a copy of 'cells' and changing the values based on the given rules.

    Parameters
    ----------
    cells : list
        The 1-dimensional list used in applying the game of life to.


    Raises
    ------
    ValueError
        If 'cells' is empty
    """

    if not cells:
        raise ValueError("evolve() cells can not be empty.")

    cells_copy = cells[:]

    for index in range(len(cells)):
        check = neighborhood(cells_copy, index)
        alive = 0
        if cells_copy[index]:
            for x in check:
                if x:
                    alive += 1
            if alive == 3 or alive == 5:
                cells[index] = cells[index]
            else:
                cells[index] = not (cells[index])

        elif not cells_copy[index]:
            for x in check:
                if x:
                    alive += 1
            if alive == 2 or alive == 3:
                cells[index] = not (cells[index])


def blinker(cells, index):
    """
    Inserts the blinker pattern into a list.

    Inserts a blinker pattern (--##--) into the list 'cells' with the
    pattern starting at the given index, 'index'.

    Parameters
    ----------
    cells : list
        The 1-dimensional list used to insert the blinker pattern
    index : int
        The index at which the blinker pattern is to be inserted in the list 'cells'.

    Raises
    ------
    ValueError
        If `index` is less than zero or if blinker pattern does not fit into list at 'index'.
    """

    right_index = min(len(cells), index + 7)

    if index < 0:
        raise ValueError("blinker() index can not be a negative value, index = ", str(index))

    if len(cells[index:right_index]) < 6:
        raise ValueError("blinker() does not fit into the list 'cells'.")

    cells[index:right_index] = False, False, True, True, False, False
