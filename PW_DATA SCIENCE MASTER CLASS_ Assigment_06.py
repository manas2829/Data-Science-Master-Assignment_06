#!/usr/bin/env python
# coding: utf-8

# # Assignment_05-02-2023

# ## 1. Explain Class and Object with respect to objected orient programming. Give suitable Example.
# 
# ### Ans:-
# 
#             Class and Object are two fundamental concepts in Object-Oriented Programming (OOP).
#             
#             1.A class is a blueprint or a template for creating objects. It defines the properties and behaviors 
#             that an object of that class will have. A class acts as a blueprint for creating objects and these 
#             objects are called instances of the class.
#             
#             2.An object is an instance of a class. It represents a real-world entity that has attributes (data) 
#             and behaviors (methods). An object is a specific occurrence of a class and contains its own set of 
#             data and methods.
# 
# 
#     Here is an example to help understand the concept of class and object in OOP:
# 
#            Suppose we have a class named "Person." This class will have data members such as name, age, and address 
#            and methods like eat, sleep, and talk. These data members and methods represent the properties and behaviors
#            of a person.
#            
#            Now, we can create an instance of the "Person" class, say "John." John is an object of the class "Person" 
#            and has his own set of data members, such as name = "John", age = 25, and address = "123 Main Street."
#            
#                                            So, in this example, the class "Person" is the blueprint or template for
#                                            creating objects, and "John" is an object of that class, representing a s
#                                            pecific person with his own set of data and behavior.

# ## 2. Name Four Pillars of OOps.
# 
# ### Ans:-
#        The four pillars of Object-Oriented Programming (OOP) are:---
#        
#        1.Abstraction: Abstraction is the process of hiding complex implementations and exposing only the essential 
#        features of an object to the user. It means providing a clear and simple interface for the user to interact 
#        with the objects without having to worry about the underlying details.
#        
#        2.Encapsulation: Encapsulation is the mechanism of wrapping up the data (attributes) and behavior (methods) 
#        within a single unit or object. It helps in keeping the data and behavior of an object protected and secure 
#        from external access and accidental modification.
#        
#        3.Inheritance: Inheritance is the mechanism by which a new class is derived from an existing class. The derived 
#        class is called a subclass and the existing class is called the superclass. Inheritance allows a subclass to 
#        inherit all the properties and behaviors of its superclass, and to add or override its own properties and behaviors.
#        
#        4.Polymorphism: Polymorphism is the ability of an object to take on multiple forms. It allows objects of different
#        classes to be treated as objects of a common class, and to be manipulated through a common interface. Polymorphism
#        enables objects to behave in multiple ways, depending on the context in which they are used.
#        
#        

# ## 3. Explain why the __inti__() function is used . Give a suitable example.
# 
# ## Ans:- 
# 
#             The __init__ method, also known as the constructor method, is a special method in Python that is automatically
#             called when an object of a class is created. It is used to initialize the attributes of an object when it is
#             created.

# In[1]:


#The __init__ method is defined within the class and has the following syntax:
def __init__ (self,[agr1,agr2,agr3'.....]) ## self is constructor 


# ### 
#        The self keyword refers to the object being created and the square brackets indicate that the arguments inside them 
#        are optional. The __init__ method takes the arguments specified within the square brackets and sets the initial 
#        values of the object's attributes.

# In[2]:


class family:
    
    def __init__(self,phone_number,email_id,gender,relationship):
        
        self.phone_number = phone_number
        self.email_id = email_id
        self.gender = gender
        self.relationship = relationship
        
    def print_details(self):
        print(f"phone_number:{self.phone_number}\n email_id:{self.email_id}\n gender :{self.gender}\n relationship :{self.relationship}")

my_family= family(9826470741,"pandey.manasranjan@gmail.com","male","father")
my_family.print_details()
 


# ### 
# 
#       In this example, the __init__ method is used to initialize the phone_number, email_id,gender and relationship 
#       attributes of the Family class when an object of the faimaly class is created. The print_details method is then 
#       used to print the values of these attributes. When the my_family object is created and the print_details method 
#       is called, the following output is in avove:
#       
#       In conclusion, the __init__ method is used to initialize the attributes of an object when it is created and is 
#       a crucial part of the object creation process in OOP.

# ## 4. Why self is used in OOps?
# 
# ## Ans:-
# 
#            In Object-Oriented Programming (OOP), the self keyword is used to refer to the instance of the class being o
#            perated on. It is used within the methods of a class to access and modify the attributes of the class.
#            
#            In conclusion, the self keyword is used in OOP to refer to the instance of the class being operated on and is
#            used to access the attributes and methods of the class within the class methods.

# ## 5. What is inheritance ? Give an example for each type of inheritance.
# 
# ### Ans:-
# 
#            Inheritance is a mechanism in Object-Oriented Programming (OOP) that allows a new class to be derived from an existing class, inheriting all its properties and behaviors. The derived class is called the subclass and the existing class is called the superclass. The subclass can inherit all the properties and behaviors of the superclass, and can also add or override its own properties and behaviors.
#            
#            There are two types of inheritance in OOP, which is in given below
#            
#            1.Single Inheritance: Single inheritance occurs when a subclass is derived from a single superclass. 
#            This is the simplest form of inheritance where a subclass inherits the properties and behaviors of a 
#            single superclass.
#            
#            2.Multi-level Inheritance: Multi-level inheritance occurs when a subclass is derived from a superclass, which is
#            itself derived from another superclass. In this case, the subclass inherits the properties and behaviors of its
#            immediate superclass, as well as all the properties and behaviors of its indirect superclass.
#            

# In[3]:


## Example of Single Inheritance 

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def print_details(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}")
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        super().__init__(make, model, year)
        self.num_doors = num_doors
        
    def print_details(self):
        super().print_details()
        print(f"Number of doors: {self.num_doors}")
        
my_car = Car("Toyota", "Camry", 2020, 4)
my_car.print_details()

