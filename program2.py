x = float(input("Input an x value: "))
y =  float(input("Input a y value: "))
z = float(input("Input a z value: "))
if x <= y <= z:
 print("True")
elif z <= y <= x:
 print("True")
else:
 print("False")