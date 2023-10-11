x = 5

y = 0.0

m = 1.0

while x > 1:
    print(y, x, m)
    y = y + (x % 2) * m
    x = x / 2 
    m = m * 10
    print(y)