from math import pi

decimal = int(raw_input("Specify decimal: "))

print float(str(pi)[:2] + str(pi)[2:decimal+2])