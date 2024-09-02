# Documentation for Python Turtle Graphics

## Overview
Python Turtle Graphics for Kids is an educational project designed to introduce beginners, especially kids, to programming through Python's Turtle graphics module.
The project includes various scripts that teach fundamental programming concepts and help users create graphical patterns and animations with Turtle.

## Functionality

### Models

#### Drawing

- **`draw_square(turtle, size)`**
  - Draws a square with created turtle pen and its size.

- **`draw_circle(turtle, radius)`**

  - Draws a circle with accepting a turtle pen and radius as parameters.

#### Patterns

- **`create_spiral_pattern(turtle, line_length)`**

  - Returns a spiral pattern with created turtle pen and the lines lenght.

- **`draw_flower(turtle, petals, radius)`**

  - Draws a flower where turtle is the pen,petals - number of petals,radius - radius of each petal.

#### Animations

- **`move_turtle(turtle)`**

  - Makes the object move thus creating an animation.

- **`bounce_ball(turtle)`**
  - Creates a bouncing ball animation.

## Implementation details
You can find all the code details by referring to it Readme.md file in the provided repository.
### Draw
This feature is found in draw directory and contains implementation details to draw square and circle. We can create all other shapes by referring to Readme.md file in the provided repo.

### Patterns
Contains two patterns and its implementation.

### Animations
Contains basic animations to understand concept of Python Turtle Graphics.

# Code Example
```python
import turtle as t
T = t.Turtle()

def draw_square(turtle, size):
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

draw_square(T,100)
```
