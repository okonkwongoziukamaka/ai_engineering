# a program function that can calcultate the area of a triangle

def calculate_tringle_area(base, height):
    if not isinstance(base, (int,float)):
        raise ValueError("base must be float or integer")
    elif not isinstance(height, (int, float)):
        raise ValueError("height must be float or an integer")
    else:
        area = 0.5 * base * height
        print(area)

try:
    calculate_tringle_area(9, 12)
except Exception as e:
    print(e)