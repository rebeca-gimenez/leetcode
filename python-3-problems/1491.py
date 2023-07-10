'''
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] 
is the salary of the ith employee.

Return the average salary of employees excluding the minimum and 
maximum salary. Answers within 10^-5 of the actual answer will be accepted.
3 <= salary.length <= 100
1000 <= salary[i] <= 106
All the integers of salary are unique.
'''
def average2(salary):
    minimum = salary[0]
    maximum = salary[0]
    for num in salary:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    salary.remove(minimum)
    salary.remove(maximum)
    return sum(salary)/len(salary)

def average(salary):
    salary.sort()
    salary.pop(0)
    salary.pop(-1)
    return sum(salary)/len(salary)
salary = [4000,3000,1000,2000]
output = 2500.00000
print(average(salary))
salary = [1000,2000,3000]
output = 2000.00000
print(average(salary))