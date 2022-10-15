from K_map_gui_tk import *
from work import *

"""
Class kmap is the wrapper for the tkinter gui.
Usage: kmap(<kmap values in list of list form>)
example for 2 input k-map, kmap([[1,0],[0,0]])
        for 3 input k-map, kmap([[1,0,0,1],[0,0,0,1]])
        for 4 input k-map, kmap([[1,0,0,1],[0,0,0,1],[0,1,0,1],[0,1,0,1]])

To draw the region, use api root.draw_region(x1,y1,x2,y2,"fill colour")
Here x1,y1 is the index for the top left corner of the region
x2,y2 is the index for the bottom right corner of the region.
Fill colour options = ['red', 'blue', 'green', 'yellow']
"""

# ====================== TEST CASES FOR 2 TERMS ======================

k_map = [['x', 1], [0, 'x']]

term = [0, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [1, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [None, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [1, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [None, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [0, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [1, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

term = [None, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'red')
root.mainloop()

# ====================== TEST CASES FOR 3 TERMS ======================

k_map = [['x', 1, 'x', 0], [1, 'x', 0, 0]]

term = [1, 1, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [0, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, None, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [0, 1, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 1, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 0, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, None, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, 1, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 1, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, None, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [0, None, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, None, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, 0, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

# ====================== TEST CASES FOR 4 TERMS ======================

k_map = [[0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0]]

term = [1, 1, 1, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [0, 0, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, None, None, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 0, 0, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 1, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 0, 1, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, None, None, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, 1, None, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [1, None, 1, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, 0, 0, None]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, None, 0, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

term = [None, 0, None, 0]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
root = kmap(k_map)
root.draw_region(lx, ly, rx, ry, 'blue')
root.mainloop()

# ====================== TEST CASE FOR 5 TERMS ======================

k_map = [[0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0],
         [0, 1, 1, 0], ['x', 1, 'x', 0], [1, 0, 0, 0], [1, 'x', 0, 0]]

term = [1, None, 0, None, 1]
((lx, ly), (rx, ry), v) = is_legal_region(k_map, term)
print((lx, ly), (rx, ry), v)
