### Exercise 13 - Curso em Video
## Develop an algorithm to read a product price and show a 5% discount

currentprice = float(input('What is the current price of this product? '))
discount = 0.05
newpricedisc = currentprice*discount
newprice = currentprice-newpricedisc

print('The new price of this product is: ${:0.2f} '.format(newprice))
