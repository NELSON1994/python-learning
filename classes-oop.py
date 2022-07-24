class Employee:
    # 'Common base class for all employees'
    empCount = 0

    # constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


# Creating Instance Objects
emp1 = Employee("Zara", 2000)

emp1.displayEmployee()
emp1.displayEmployee()

#garbage collection
# python does automatic garbage collection through
# __del__() destructor

class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print(class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
# printid(pt1), id(pt2), id(pt3) # prints the ids of the obejcts
del pt1
del pt2
del pt3