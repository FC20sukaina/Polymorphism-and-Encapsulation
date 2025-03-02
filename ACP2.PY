def calculate_area(length, width):
    area = length*width
    return area

result = calculate_area(5, 3)
print("My area is: ",result)

def find_area(Base, Height):
    Area = 1/2 * (Base * Height)
    return Area

Base = 2  #c.m
Height = 4 #c.m

Area = find_area(Base, Height)
print("My area is: ",1/2 * Base * Height)