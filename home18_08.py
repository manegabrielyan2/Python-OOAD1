#book library
# class Book:
#     def __init__(self ):
#         self._title = ''
#         self._author = ''
#     def settitle(self , title):
#         if not (isinstance(title , str) or title == ''):
#             raise ValueError('Title is not entered correctly')
#         self._title = title
#     def setauthor(self , author):
#         if not (isinstance(author , str) or author == ''):
#             raise ValueError('Title is not entered correctly')
#         self._author = author
#     def gettitle(self):
#         return self._title
#     def getauthor(self):
#         return self._author    
#     def __str__(self):
#         pass
# class Library:

#     def __init__(self ):
#         self.lib = []
        
#     def add_book(self , book):
#         self.lib.append(book)

#     def rem_book(self , title , author):
#         for i in self.lib:
#             if i.gettitle()  == title and i.getauthor() == author :
#                 self.lib.remove(i)

#     def list_books(self ):
#         for i in self.lib:
#             print(f'title: {i.gettitle()} , author: {i.getauthor()}')



#Course
# class Student:
#     def __init__(self ):
#         self._name = ''
#         self._age = 0
#     def getname(self):
#         return self._name
#     def setname(self , name):
#         if (not isinstance(name , str) or name == ''):
#             raise ValueError('Name cannot be empty')
#         self._name = name

#     def getage(self):
#         return self._age
#     def setage(self , age):
#         if (not isinstance(age , int) or age < 0):
#             raise ValueError('Credit cannot be negative')
#         self._age = age
# class Course:
#     def __init__(self):
#         self.students = []
#         self._name = ''
#         self._credit = 0
#     def getname(self):
#         return self._name
#     def setname(self , name):
#         if (not isinstance(name , str) or name == ''):
#             raise ValueError('Name cannot be empty')
#         self._name = name
#     def getcredit(self):
#         return self._credit
#     def setdredit(self , credit):
#         if (not isinstance(credit , int) or credit < 0):
#             raise ValueError('Credit cannot be negative')
#         self._credit = credit
#     def add_student(self , stud):
#         self.students.append(stud)
#     def list_det(self):
#         print(f"Course name : {self._name} and course credit: {self._credit}")
#         for i in self.students:
#             print(f'student name: {i}')

# class Department:
#     def __init__(self):
#         self.courses = []
#         self._name = ''
#     def getname(self):
#         return self._name
#     def setname(self , name):
#         if (not isinstance(name , str) or name == ''):
#             raise ValueError('Name cannot be empty')
#         self._name = name
#     def add_course(self , course):
#         self.courses.append(course)
 
#project
# class Project:
#     def __init__(self):
#         self._name = ''
#         self._description = ''
#         self.employees = []
#     def setname(self , name):
#         if not isinstance(name , str) or name == '':
#             raise ValueError('Name cannot be empty')
#         self._name = name
#     def getname(self):
#         return self._name
#     def setdescription(self , description):
#         if not isinstance(description , str) or description == '':
#             raise ValueError('Description cannot be empty')
#         self._description = description
#     def getdescription(self):
#         return self._description
    
#     def add_employee(self , emp):
#         self.employees.append(emp)
#     def list_det(self):
#         print(f'project name : {self._name}')
#         print(f'Description for project : {self._description}')
#         print('Employees involved in the project:')
#         for emp in self.employees:
#             print(emp)

# class Company:
#     def __init__(self):
#         self._name = ''
#         self.projects = []
#     def setname(self , name):
#         if not isinstance(name , str) or name == '':
#             raise ValueError('Name cannot be empty')
#         self._name = name
#     def getname(self):
#         return self._name
#     def add_project(self , project):
#         self.projects.append(project)
#     def track(self ):
#         print('Here are current projects and employees involved:')
#         for project in self.projects:
#             print(f"project : {project} and employees:")
#             for emp in project.employees:
#                 print(emp)

#person
class Person:
    def __init__(self , name , age):
        self._name = name
        self._age = age
    def setname(self , name):
        if not isinstance(name , str) or name == '':
            raise ValueError('Name cannot be empty')
    def getname(self):
        return f'name:{self._name}'
    def getage(self):
        return f'age : {self._age}'
    def setage(self , age):
         if (not isinstance(age , int) or age < 0):
             raise ValueError('Credit cannot be negative')
         self._age = age

class Employee(Person):
    def __init__(self , name , age , id , department):
        super().__init__( name , age )
        self._ID = id
        self._department = department
    def set_id(self , ID):
        if not isinstance(ID , int):
            raise ValueError('ID must be a number')
        self._ID = ID
    def get_ID(self):
        return self._ID
    def set_department(self , dep):
        if not isinstance(dep , str) or dep == '':
            raise ValueError('Department is entered incorrectly')
        self._department = dep 
    def get_department(self):
        return self._department

obj = Employee('Mane' , 20 , 1 , 'Bio')

print(obj.get_department())

    

#Department
class Department:
    def __init__(self):
        self._name = ''
        self.employees = []
    def setname(self , name):
        if (not isinstance(name , str) or name == ''):
            raise ValueError('Name passed incorrectly')
        self._name = name
    def getname(self):
        return self._name 
    def add_employee(self , emp):
        self.employees.append(emp)

    def list_details(self):
        print(f'company name: {self._name}')
        print("Employees of department:")
        for emp in self.employees:
            print(emp)

class Company:
    def __init__(self):
        self._name = ''
        self.departments = []
    def setname(self , name):
        if (not isinstance(name , str) or name == ''):
            raise ValueError('Name is entered incorrectly')
        self._name = name
    def getname(self):
        return self._name
    def add_dep(self , dep):
        self.departments.append(dep)
    def remove_dep(self , dep):
        for i in self.departments:
            if i.getname() == dep:
                self.departments.remove(i)
    def list_deps(self):
        print(f'Departments of {self._name} company:')
        for i in self.departments:
            print(i.getname())



