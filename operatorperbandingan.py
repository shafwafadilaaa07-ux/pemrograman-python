#opertaor != (tidak sama dengan)
x = 5
y = '5'

z = x != y #true
print(z)

#operator > lebih besar dari 
a = 7 > 4 #true
print(a)

b = 25 < 23 #false
print(b)

#operator logika and, OR, NOT
logikaAnd = z & a
logikaAndLagi = z and b
print(logikaAnd) #true
print(logikaAndLagi) #false

#operator OR
logikaOr = z or b
print(logikaOr) #true

#opertor NOT
logikaNot = not(z)
print(logikaNot) #false