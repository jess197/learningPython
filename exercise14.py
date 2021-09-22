### Exercise 14 - Curso em Video
## Develop an algorithm to read a employee salary and show a 15% salary increase

currentsalary = float(input('What is your current salary? '))
salaryIncrease = 0.15
newsalary = currentsalary+(currentsalary*salaryIncrease)

print('With a salary increase of 15% your new salary is: $ {:0.2f} '.format(newsalary))


