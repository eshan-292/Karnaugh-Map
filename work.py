
"""
The code works for any n*m k-map for any number of variables.
"""

from K_map_gui_tk import *

# Returns integer lagarithm of number "n" to the base 2
def log(n):
    ans = 0
    while (n >= 2):
        ans += 1
        n //= 2
    return ans

# Convert a normal cartesian coordinate into a k-map coordinate
def kmap_index(size, col, row, h_ind, v_ind, rev_col, rev_row):
    if col > 0:
        if rev_col:
            if h_ind//col == 0:
                return col*(1 - h_ind//col) + kmap_index(size, col//2, row, h_ind % col, v_ind, not rev_col, rev_row)
            else:
                return col*(1 - h_ind//col) + kmap_index(size, col//2, row, h_ind % col, v_ind, rev_col, rev_row)
        else:
            if h_ind//col == 1:
                return col*(h_ind//col) + kmap_index(size, col//2, row, h_ind % col, v_ind, not rev_col, rev_row)
            else:
                return col*(h_ind//col) + kmap_index(size, col//2, row, h_ind % col, v_ind, rev_col, rev_row)
    elif row > 0:
        if rev_row:
            if v_ind//row == 0:
                return size*row*(1 - v_ind//row) + kmap_index(size, col, row//2, h_ind, v_ind % row, rev_col, not rev_row)
            else:
                return size*row*(1 - v_ind//row) + kmap_index(size, col, row//2, h_ind, v_ind % row, rev_col, rev_row)
        else:
            if v_ind//row == 1:
                return size*row*(v_ind//row) + kmap_index(size, col, row//2, h_ind, v_ind % row, rev_col, not rev_row)
            else:
                return size*row*(v_ind//row) + kmap_index(size, col, row//2, h_ind, v_ind % row, rev_col, rev_row)
    else:
        return 0

# Returns decimal form of a binary number "bin"
def bin2Dec(bin):
    dec = 0
    for i in range(len(bin)):
        dec += dec + bin[i]
    return dec

# Returns the list of all the "terms" contained in the condensed "term"
def term2Tuple(term, terms, start):
    isNone = False
    firstNone = 0
    for i in range(start, len(term)):
        if term[i] is None:
            isNone = True
            firstNone = i
            break
    if isNone:
        term[firstNone] = 0
        term2Tuple(term, terms, firstNone + 1)
        term[firstNone] = 1
        term2Tuple(term, terms, firstNone + 1)
        term[firstNone] = None
    else:
        terms.append(term.copy())

# Returns the cartesian coordinates of the region
# Returns TRUE if the "term" is legal in the "kmap" else FALSE
def is_legal_region(kmap_function, term):
    row = len(kmap_function)
    col = len(kmap_function[0])
    terms = []
    term2Tuple(term, terms, 0)
    isLegal = True
    indices = [0]*(row*col)
    minInd = col*row
    maxInd = 0
    for newTerm in terms:
        h = bin2Dec(newTerm[:log(col)])
        v = bin2Dec(newTerm[log(col):])
        k = kmap_index(col, col, row, h, v, False, False)
        indices[k] = 1
        minInd = min(minInd, k)
        maxInd = max(maxInd, k)
        if (kmap_function[k//col][k % col] == 0):
            isLegal = False
    lx = minInd//col
    ly = minInd % col
    rx = maxInd//col
    ry = maxInd % col
    for index in range(ly, ry+1):
        if indices[lx*col + index] == 0:
            ly, ry = ry, ly
            break
    for index in range(lx, rx+1):
        if indices[index*col + ly] == 0:
            lx, rx = rx, lx
            break

    return ((lx, ly), (rx, ry), isLegal)


"""
TEST CASES START HERE
Please uncomment the test case you want to run
"""

# # ====================== TEST CASES FOR 2 TERMS ======================

# k_map = [['x', 1], [0, 'x']]

# term = [0, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [1, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [None, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [1, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [None, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [0, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [1, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# term = [None, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'red')
# root.mainloop()

# # ====================== TEST CASES FOR 3 TERMS ======================

# k_map = [['x', 1, 'x', 0], [1, 'x', 0, 0]]

# term = [1, 1, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [0, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, None, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [0, 1, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 1, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 0, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, None, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, 1, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 1, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, None, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [0, None, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, None, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, 0, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# # ====================== TEST CASES FOR 4 TERMS ======================

# k_map = [[0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0]]

# term = [1, 1, 1, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [0, 0, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, None, None, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 0, 0, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 1, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 0, 1, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, None, None, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, 1, None, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [1, None, 1, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, 0, 0, None]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, None, 0, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# term = [None, 0, None, 0]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
# root = kmap(k_map)
# root.draw_region(lx, ly, rx, ry, 'blue')
# root.mainloop()

# # ====================== TEST CASE FOR 5 TERMS ======================

# k_map = [[0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0],
#          [0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0]]

# term = [1, None, 0, None, 1]
# ((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
# print((lx, ly), (rx, ry), v)
