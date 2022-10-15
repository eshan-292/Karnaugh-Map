# Karnaugh-Map
For a given K map and a term, this program highlights the region corresponding to the term and also reports whether the region is legal or illegal


# Our Approach

We have employed the following approach to solve the problem:  
1. Evaluate the list of terms that together represent the condensed term.  
2. Now, every term in the above list represents a point on the k-map.  
3. Convert every term in the above list into indices in the k-map coordinate system.  
4. If the k-map contains 1/‘x’ at all the above indices, report TRUE else report FALSE.  
5. Next, let the upper-most leftmost coordinate be (lx, ly) and the bottom-most right- most coordinate be (rx, ry).  
6. Since, the k-map is circular/continuous through its edges, check if all the points between (lx,ly) and (rx,ry) are legal. If not, swap ry,ly and rx,lx accordingly. Finally report (lx, ly), (rx, ry).  

# Testing

We have done exhaustive testing of our program for functions of 2, 3 and 4 variables, covering all possibilities to ensure the correctness of our code. We have attached the screenshots of the GUI output for each of the test cases in the report.  


