from math_operation.basic_operation import Arithmetic
from math_operation.geometry import Area

print("Arithmetic operations:")
print("5 + 3=", arithmetic.add(5,3))
print("10 - 7=", arithmetic.subtact(10,7))
print("5 * 3=", arithmetic.multiply(5,3))
print("8 / 2=",arithmetic.divide(8,2))
print("8 / 0=",arithmetic.divide(8,0))

print("\nArea calculations:")
print("Rectangle (lengtyh=5,width=3):",Area.Reactangle_Area(5,3))
print("Circle (radius=7):",Area.circle_area(7))
print("Triangle (base=4,height=5):",Area.tiangle_Area(4,5))
