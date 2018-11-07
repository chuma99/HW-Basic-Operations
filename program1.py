import math as m
t = float(input("Input a Temperature (F): "))
v =  float(input("Input a Wind Speed (mph): "))
w = 35.74 + (0.6215*t) + ((0.4275t)-35.75)(v**0.16)
print("The wind chill:",w)