import random

# We are going to simulate a consulting company starting up from a one man show into an extremely large corporation
# so that we can taker closer look at how agency effects change at scale

class Employee:
    def __init__(self, salary, earning_potential):
        self.salary = salary
        self.earning_potential = earning_potential

class Project():
    def __init__(self):
        self.effort_remaining = 100
        self.payoff = 100


jim = Employee(salary=200, earning_potential=150)


# We need some model of the contract lifecycle
# We are going to need to land projects, we are then going to need to do the work to complete those projects
# which will finally result in revenue for the company
cash = 10000
projects = []
company_employees = [jim]
for timestep in range(100):
    # Pay salaries
    cash -= sum(employee.salary for employee in company_employees)

    # Get projects
    if random.random() > 0.2:
        projects.append(Project())

    # Earn money
    cash += sum(employee.earning_potential for employee in company_employees)

    # Check if we are bankrupt    
    if cash <= 0:
        print("Bankruptcy in timestep:" + str(timestep))
        break