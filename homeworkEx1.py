# import os
# os.system("clear")
#Exercise 1:

#Create a class Dog. Make sure it has the attributes name, breed, color, gender. There are no methods in this class. The main function below should work with the class you create.

# class Dog():
#     def __init__(self, name="", breed="", color="", gender=""):
#         self.name = name
#         self.color = color
#         self.breed = breed
#         self.gender = gender
#
# def main():
#     newDog = Dog ("Fiddo", "Lab", "brown", "male")
#     print(newDog.name)
#     print(newDog.breed)
#     print(newDog.color)
#     print(newDog.gender)
#
# if __name__ == '__main__':
#     main()

#Exercise 2: Create a To Do class. Create the attributes: name, dueDate, list (this should be an array). There should not be a method in this class. The main function below should work with the class you create.
# class ToDo():
#     def __init__(self, name="",dueDate="",list=""):
#         self.name=name
#         self.dueDate=dueDate
#         self.list=list
#
#
# def main():
#     newToDoList = ToDo("Kenn", "Next Week", ["Do the dishes", "Wash your clothes"])
#     print(newToDoList.list)
#
# main()
#
# #Exercise 3: Continue with Exercise 2, but create a method that will append a string variable to the list. The main function should look like this now
#
class ToDo():
     def __init__(self, name="",dueDate="",list=""):
         self.name=name
         self.dueDate=dueDate
         self.list=list

     def addTask(self, newTask):
             self.list.append(newTask)

def main():
    newToDoList = ToDo("Kenn", "Next Week", ["Do the dishes", "Wash your clothes"])
    print(newToDoList.list)
    newToDoList.addTask("Take out the trash")
    print(newToDoList.list)

if __name__ == '__main__':
     main()