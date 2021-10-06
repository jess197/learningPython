### Exercise 37 - Curso em Video
## Develop a program to approve a bank loan to buy a house. Calculate the monthly payment in installments, knowing that can't ultrapass 30% of your salary.

house = float(input('How much is the house? '))
salary = float(input('What is your salary?  '))
years = int(input('In how many years do you pretend to totally pay the loan? '))


montly = years*12
payment_per_month = house/montly
percent_of_salary = (salary*130/100)-(salary)

if(payment_per_month > percent_of_salary):
    print("The montly payment needed to buy this house is {:0.2f}. You can't pay this, so your loan is denied".format(payment_per_month))
else:
    print('Congratulations, your loan is approved! You will need to pay: ${:0.2f} montly'.format(payment_per_month))


