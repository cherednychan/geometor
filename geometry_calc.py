import math #need it for pi and sqrt

def square(side):
    perimeter = 4 * side
    area = side ** 2
    return perimeter, area

def rectangle(x1, y1, x2, y2):
    length = abs(x1 - x2) #calcutaing the length using coordinates
    width = abs(y1 - y2) #same with width
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

def circle(radius):
    perimeter = 2 * math.pi * radius
    area = math.pi * (radius ** 2)
    return perimeter, area

def triangle(x1, y1, x2, y2, x3, y3):
    side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) #calcutaing the first side using coordinates; same with second and third
    side2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    perimeter = side1 + side2 + side3
    s = perimeter / 2 
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3)) #Heron's formula
    return perimeter, area

def main():
    while True:
        shape_type = input("Please enter the figure type (Square, Rectangle, Circle, Triangle) or 'exit' to quit: ").strip().capitalize()
        if shape_type == "Exit":
            print("Goodbye!")
            break

        if shape_type == "Square":
            side = float(input("Enter the side length of the square: ")) #we need to know just one side of square to calculate the area and perimeter
            perimeter, area = square(side)

        elif shape_type == "Rectangle":
            x1 = float(input("Enter the x-coordinate of the top-right corner of the rectangle: "))
            y1 = float(input("Enter the y-coordinate of the top-right corner of the rectangle: "))
            x2 = float(input("Enter the x-coordinate of the bottom-left corner of the rectangle: "))
            y2 = float(input("Enter the y-coordinate of the bottom-left corner of the rectangle: "))
            perimeter, area = rectangle(x1, y1, x2, y2)

        elif shape_type == "Circle":
            radius = float(input("Enter the radius of the circle: ")) #same as with square: we need just the radius
            perimeter, area = circle(radius)

        elif shape_type == "Triangle":
            x1 = float(input("Enter the x-coordinate of the first point of the triangle: "))
            y1 = float(input("Enter the y-coordinate of the first point of the triangle: "))
            x2 = float(input("Enter the x-coordinate of the second point of the triangle: "))
            y2 = float(input("Enter the y-coordinate of the second point of the triangle: "))
            x3 = float(input("Enter the x-coordinate of the third point of the triangle: "))
            y3 = float(input("Enter the y-coordinate of the third point of the triangle: "))
            perimeter, area = triangle(x1, y1, x2, y2, x3, y3)

        else:
            print("Invalid shape type. Please try again.")
            continue
    
        print(f"{shape_type} Perimeter: {perimeter}; Area: {area}.\n") #print the final results
        break #stop after showing the results

if __name__ == "__main__": #execute the main function
    main()

