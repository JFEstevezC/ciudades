from string import octdigits


print("-------------------------------------------------------------------")
print("-----------------------CRECIMIENTO CIUDADES------------------------")
print("-------------------------------------------------------------------")

print("Año de inicio: 1980 ")
A = 3.5
B = 5
año = 1980

while A < B:

    A = A + A * (7/100)
    B = B + B * (5/100)
    año = año + 1

print ("El año es: " + str (año))