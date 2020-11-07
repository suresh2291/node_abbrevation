'''
Approach:
A point lies inside or not the rectangle if and only if 
it’s x-coordinate lies between the x-coordinate of the given bottom-right and top-left coordinates of the rectangle
and y-coordinate lies between the y-coordinate of the given bottom-right and top-left coordinates.
checking the points lies inside or outside of a  given rectangle

if it lies print yes else print no 
'''

#Declaring a rectangle
x1 , y1 , x2 , y2 = 0, 0, 10, 8
 
points = [(6, 2), (3, 4), (7,10), (10,20)]#declare the points to check inside the rectangle.

sort_x_coordinate = sorted(points, key=lambda x: x[0]) 
print(sort_x_coordinate)

sort_y_coordinate = sorted(points, key=lambda y: y[1]) 
print(sort_x_coordinate)

#sort by X Coordinate
for x, y in sort_x_coordinate:
    if (x >= x1 and x <= x2 and 
         y >= y1 and y <= y2) : 
        print("Yes")
    else : 
         print("No")

#sort by Y coordinaate
for x, y in sort_y_coordinate:
    if (x >= x1 and x <= x2 and 
         y >= y1 and y <= y2) : 
        print("Yes")
    else : 
         print("No")
         
          