m = float(input("Input a Numerical Month: "))
d =  float(input("Input a date: "))
y = float(input("Input a year: "))

y1 = y - (14-m)/12
x = y1 + (y1/4) - (y1/100) + (y1/400)
m1 = m + 12 * ((14-m)//12) - 2
d1 = (d + x + (31*m1)//12) % 7

if d1 = 0:
 print("That date was a Sunday")
elif d1 = 1:
 print("That date was a Monday")
elif d1 = 2:
 print("That date was a Tuesday")
elif d1 = 3:
 print("That date was a Wednesday")
elif d1 = 4:
 print("That date was a Thursday")
elif d1 = 5:
 print("That date was a Friday")
elif d1 = 5:
 print("That date was a Saturday") 
else:
 print("Error")