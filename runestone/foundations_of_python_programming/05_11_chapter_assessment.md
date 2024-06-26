# 5.11. Chapter Assessment - Turtle and Object Mechanics

What are correct ways to tell a turtle named Tex to move forward 20 pixels?
Select as many as apply.

- [X] A. Tex.forward(20)
- [ ] B. forward() + 20
- [ ] C. forward(20)
- [ ] D. forward(20).Tex
- [X] E. Tex.forward(10 + 10)

        A. This is a correct way to move turtle forward.
        E. You are allowed to write expressions inside methods, so this is correctly written.

Which is the correct way to make a new instance of the Turtle class?

- [ ] A. turtle(Turtle)
- [X] B. turtle.Turtle()
- [ ] C. Turtle.turtle()
- [ ] D. Turtle(turtle)

        Yes, this is the correct way.

What does each instance of the Turtle class represent?

- [] A. The turtle class.
- [] B. The same turtle that is used in each drawing your programs make.
- [X] C. A unique 'turtle' that you can use to draw.

        Yes, an instance of the turtle class represents a unique turtle. The turtle class is like a stencil or mold that can be used to make as many turtles as you would like.

Select all of the following things that methods can do:

- [X] A. Change the value of an attribute.
- [X] B. Return values.
- [X] C. Create new attributes of an instance and set their values.
- [ ] D. Delete object instances.
- [ ] E. None of the above.

        A. Methods can change the value that is associated with an attribute.
        B. Methods can return values.
        C. Attributes do not need to be pre-declared; any code can add a new attribute to an instance just by assigning a value to it.

For an instance of a class that is assigned to the variable student, what is
the proper way to refer to the title attribute/instance variable?

- [ ] A. student.title()
- [ ] B. title.student()
- [ ] C. title.student
- [ ] D. student(title)
- [X] E. student.title

        Yes, this is the correct syntax to use.

What is the name of jane’s attribute (not method) that is referred to in the following code?

```python
import turtle

jane = turtle.Turtle()
jane.forward(20)
print(jane.x)
```

The attribute is
        
        x

        Good work!

What are the names of the instances in the following code? Please put one instance
per blank space and enter them in the order that the computer would read them.

```python
import turtle
wn = turtle.Screen()

jazz = turtle.Turtle()
jazz.forward(50)
jazz.right(90)
pop = turtle.Turtle()
pop.left(180)
pop.forward(76)
```

        | wn      | jazz       | pop

        - Good work!
        - Good work!
        - Good work!
