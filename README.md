# Python_Classes_Homework

#### Exercise 1:
Create a class Dog. Make sure it has the attributes name, breed, color, gender. There are no methods in this class. The main function below should work with the class you create.

```python
class Dog():
  CLASS HERE

def main():
	newDog = Dog(“Fiddo”, “Lab”, “brown”, “male”)
	print(newDog.name)
	print(newDog.breed)
	print(newDog.color)
	print(newDog.gender)

main()
```


#### Exercise 2:
Create a ToDo class. Create the attributes: name, dueDate, list (this should be an array). There should not be a method in this class. The main function below should work with the class you create.

```python
class ToDo():
	CLASS HERE

def main():
	newToDoList = ToDo(“Kenn”, “01/01/1990”, [“Do the dishes”, “Wash your clothes”])
	print(newToDoList.list)

main()
```

#### Exercise 3:
Continue with Exercise 2, but create a method that will append a string variable to the list. The main function should look like this now:

```python
class ToDo():
	CLASS HERE

def main():
	newToDoList = ToDo(“Kenn”, “01/01/1990”, [“Do the dishes”, “Wash your clothes”])
	print(newToDoList.list)
	newToDoList.addTask(“Take out the trash”)

main()
```
