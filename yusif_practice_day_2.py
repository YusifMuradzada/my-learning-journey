# import yusif_practice_day_1
# class Car :
#     def __init__(self,brand,year,model):
#         self.model=model
#         self.year=year
#         self.brand=brand

#     def show_info(self):
#         print(f"model :{self.model},year:{self.year},brand:{self.brand}")

# car1=Car("Chevrolet",2025,"Equinox")
# car2=Car("Toyota",2025,"Rav4")
# print("car1 info:", end="\n")
# car1.show_info()
# print("car2 info:", end="\n")
# car2.show_info()
        
        
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
#     def role(self):
#         print("I am an employee.")

#     def show_info(self):
#             print(f"name:{self.name},salary:{self.salary}")

# class Manager(Employee):
#     def __init__(self,name,salary,team_size):
#         super().__init__(name,salary)
#         self.team_size=team_size
        
#     def role(self):
#         print("I am a manager.")    
        
#     def show_info(self):
#         print(f"name:{self.name},salary:{self.salary},team_size:{self.team_size}")

# emp1=Employee("Yusif",8000)
# manager1=Manager("Yusifi",4500,10)
# print("emp1 info:", end="\n")
# emp1.show_info()
# print("manager1 info:", end="\n")
# manager1.show_info()
# people=[emp1,manager1]
# for person in people:
#     person.role()




# class Shape :
#     def __init__(self,name):
#         self.name=name
#     def area(self):
#         print(f"name:{self.name} hele hesablanmiyib ")

# class Circle(Shape):
#     def __init__(self,radius,name):
#         super().__init__(name)
#         self.radius=radius
    
#     def area (self):
#         print(f"name:{self.name} {3.14* pow (self.radius,2)}")
        
# class Rectangle(Shape):
#     def __init__(self,height,width,name):
#         super().__init__(name)
#         self.height=height
#         self.width=width
    
#     def area(self):
#         print(f"name:{self.name} {self.height * self.width}")
        
# shapes=[Circle(5,"circle"),Rectangle(10,11,"rectangle")]
# for shape in shapes :
#     shape.area()
    
        



