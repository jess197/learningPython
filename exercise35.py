### Exercise 35 - Curso em Video
## Develop a program to ask an employee salary and calculate a salary increase
# To salaries more than $1250, calculate an increase of 10%
# To salaries up to $1250, calculate an increase of 15%

salary = float(input('What is your salary? '))

if(salary < 1250):
    newsalary = salary*115/100
    print('You received a salary increase of 15%, your new salary is ${0:.2f}'.format(newsalary))
else:
    newsalary = salary * 110 / 100
    print('You received a salary increase of 10%, your new salary is ${0:.2f}'.format(newsalary))