# Session 2 of 00 - Employee Example

class Employee:
    def __init__(self, name : str, base_salary : float) --> None:
        self.name = name
        self.salary = base_salary

    def cal_bonus(self, multiplier : float) -> float:
        return self.salary * multiplier



emp = Employee("Alice", 50000.0)

bonus = emp.cal_bonus(1.1)

print(f"Bonus for {emp.name} is {bonus}")

