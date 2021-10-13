### Exercise 53 - Curso em Video
# Develop a program that reads a integer number and print if is a primes or not.

num = int(input('Type a number: '))
count = 0
for n in range(1, num+1):
    if num%n == 0:
        print('\33[34m',end='')
        count += 1
    else:
        print('\33[31m',end='')
    print('{} '.format(n),end='')
print('')
print('\33[mO número {} foi divisível {} vezes'.format(num,count))
if(count > 2):
    print('O número não é primo')
else:
    print('O número é primo')
