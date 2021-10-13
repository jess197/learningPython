### Exercise 45 - Curso em Video
## Develop a program that calculate the total price to be paid in a product, considering diferent types of payment conditions
# With Cash : 10% discount
# Credit Card : 5% discount
# 2x in Credit Card : Normal price
# 3x or more in Credit Card: 20% of fees

from time import sleep

productPrice = float(input('What is the product price? '))

print('=-'*20)
print('Payment Conditions')
print('How you will pay? ')
print('1 - Cash')
print('2 - Credit Card')
print('3 - Credit Card in 2x ')
print('4 - Credit Card in 3x or more')
print('=-'*20)
print('')
option = int(input())
print('PROCESSING...')
sleep(3)
if(option == 1):
    discount = (productPrice*110/100) - productPrice
    newProductPrice = productPrice - discount
elif(option == 2):
    discount = (productPrice*105/100) - productPrice
    newProductPrice = productPrice - discount
elif(option == 3):
    newProductPrice = productPrice
elif(option == 4):
    newProductPrice = productPrice*120/100
else:
    print('You selected a wrong option. Try Again!')
print('You choose option {}, you will need to pay {:.2f}'.format(option,newProductPrice))

