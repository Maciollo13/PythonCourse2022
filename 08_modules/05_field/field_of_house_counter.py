import fields
def rectangle_number():
    number = int(input("Input number of rectangles in house: "))
    return number

def triangle_number():
    number = int(input("Input number of triangle in house: "))
    return number

def trapezoid_number():
    number = int(input("Input number of trapezoid in house: "))
    return number

def rectangle_field(number):
    tries = 0
    field_rectangle = 0
    while number >= tries:
        dimension = input("Input dimenstions of rectangle/square [axb]:")
        dim1 = dimension[0]
        dim2 = dimension[2]
        field_rectangle += fields.rectangle(dim1, dim2)
        tries += 1
    return field_rectangle

def triangle_field(number):
    tries = 0
    field_triangle = 0
    while number >= tries:
        dimension = input("Input dimenstions of rectangle/square [axh]:")
        dim1 = dimension[0]
        dim2 = dimension[2]
        field_triangle += fields.triangle(dim1, dim2)
        tries += 1
    return field_triangle

def trapezoid_field(number):
    tries = 0
    field_trapezoid = 0
    while number >= tries:
        dimension = input("Input dimenstions of rectangle/square [axbxh]:")
        dim1 = dimension[0]
        dim2 = dimension[2]
        dim3 = dimension[4]
        field_trapezoid += fields.trapezoid(dim1, dim2, dim3)
        tries += 1
    return field_trapezoid

def main():
    sum_of_fields = 0
    rectangle = rectangle_number()
    triangle = triangle_number()
    trapezoid = trapezoid_number()
    rec_field = rectangle_field(rectangle)
    tri_field = triangle_field(triangle)
    tra_field = trapezoid_field(trapezoid)
    sum_of_fields += rec_field + tri_field + tra_field
    print(f"Sum of triangle fields is {tri_field}")
    print(f"Sum of rectangle fields is {rectangle}")
    print(f"Sum of trapezoid fields is {tra_field}")
    print(f"Field of house is {sum_of_fields}")