import sys

# Import Employee from pack1
sys.path.append("C:/Automation/PWPython/day13/pack1")
from emp import Employee
e = Employee(101, 'Scott', 40000)
e.displayemp()   # Output: empid:101 empname:Scott empsal:40000


# Import Student from pack2
sys.path.append("C:/Automation/PWPython/day13/pack2")
from pack2.stu import Student

s = Student(141, 'David', 'A')
s.displaystu()   # Output: stuid:141 stuname:David stusal:A

