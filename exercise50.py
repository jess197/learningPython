### Exercise 50 - Curso em Video
# Develop a times table like exercise number 10, but using for.
print('=-'*15)
print('TIMES TABLE FROM 1 TO 10')
print('=-'*15)
for a in range(1, 11):
    for b in range(1, 11):
        mult = a*b
        print('{} x {} = {} '.format(a, b, mult))
    print('=-'*15)


