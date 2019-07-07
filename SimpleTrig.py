import math


def cosineside(b, c, A):  # finds the length of side a
    plug = b ** 2 + c ** 2 - 2 * b * c * math.cos(math.radians(A))
    return round(math.sqrt(plug), 3)


def cosineangle(a, b, c):  # finds angle measure of A
    fraction = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    return round(math.degrees(math.acos(fraction)), 3)


def sineangle(a, A, b):  # finds angle measure of B
    return round(math.degrees(math.asin((b * math.sin(math.radians(A))) / a)), 3)


def sineside(a, A, B):  # finds the length of side b
    return round((a * math.sin(math.radians(B))) / (math.sin(math.radians(A))), 3)


def perimeter(a, b, c):
    return a + b + c


def area(a, b, c):  # heron's formula
    s = perimeter(a, b, c) / 2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)), 3)


EXPECTED_INPUTS = ["SSS", "SAS", "ASA", "AAS", "SSA"]  # Types of triangles that are solvable
def main():
    while True:  # input for what type of triangle is given
        check = input("Enter type of triangle (SSS, SAS, ASA, AAS, SSA): ").upper()
        if check in EXPECTED_INPUTS:
         break
        else:
            print("Haha. Very funny. Input invalid.")

    if check == "SSS":  # side side side
        while True:
            try:
                sideA = float(input("Enter length of side a: "))
                sideB = float(input("Enter length of side b: "))
                sideC = float(input("Enter length of side c: "))
                angleA = cosineangle(sideA, sideB, sideC)
                angleB = cosineangle(sideB, sideA, sideC)
                angleC = cosineangle(sideC, sideA, sideB)
                print('Angle A: {} Angle B: {} Angle C: {}'.format(angleA, angleB, angleC))
                break
            except ValueError:
                print("Triangle does not exist. Try again.")

    if check == "SAS":  # side angle side
        while True:
            try:
                sideB = float(input("Enter length of side b: "))
                A = float(input("Enter measure of A(degrees): "))
                sideC = float(input("Enter length of side c: "))
                sideA = cosineside(sideB, sideC, A)
                angleB = sineangle(sideA, A, sideB)
                angleC = sineangle(sideA, A, sideC)
                print('Side A: {} Angle B: {} Angle C: {}'.format(sideA, angleB, angleC))
                break
            except ValueError:
                print("Triangle does not exist. Try again.")

    if check == "ASA":  # angle side angle
        while True:
            try:
                A = float(input("Enter measure of A(degrees): "))
                sideC = float(input("Enter length of side c: "))
                B = float(input("Enter measure of B(degrees): "))
                angleC = round(180 - A - B, 3)
                sideA = sineside(sideC, angleC, A)
                sideB = sineside(sideC, angleC, B)
                print('Side A: {} Side B: {} Angle C: {}'.format(sideA, sideB, angleC))
                break
            except ValueError:
                print("Triangle does not exist. Try again.")

    if check == "AAS":  # angle angle side
        while True:
            try:
                A = float(input("Enter measure of A(degrees): "))
                B = float(input("Enter measure of B(degrees): "))
                sideA = float(input("Enter length of side a: "))
                angleC = round(180 - A - B, 3)
                sideB = sineside(sideA, A, B)
                sideC = sineside(sideA, A, angleC)
                print('Side B: {} Side C: {} Angle C: {}'.format(sideB, sideC, angleC))
                break
            except ValueError:
                print("Triangle does not exist. Try again.")

    if check == "SSA":  # side side angle
        while True:
            try:
                sideB = float(input("Enter length of side b: "))
                sideA = float(input("Enter length of side a: "))
                A = float(input("Enter measure of A(degrees): "))
                angleB = sineangle(sideA, A, sideB)
                angleC = round(180 - angleB - A, 3)
                sideC = sineside(sideA, A, angleC)
                print('Side c: {} Angle B: {} Angle C: {}'.format(sideC, angleB, angleC))
                diff = (180 - angleB) + A
                if diff < 180:
                    angleB = 180 - angleB
                    angleC = round(180 - angleB - A, 3)
                    sideC = sineside(sideA, A, angleC)
                    print('Side c: {} Angle B: {} Angle C: {} There are two solutions'.format(sideC, angleB, angleC))
                break
            except ValueError:
                print("Triangle does not exist")

    check = input("Would you like to know the perimeter (y/n)? ").lower()
    if check == "y":
        print('Perimeter: {}'.format(perimeter(sideA, sideB, sideC)))

    check = input("Would you like to know the area (y/n)? ").lower()
    if check == "y":
        print('Area: {}'.format(area(sideA, sideB, sideC)))


if __name__ == '__main__':
    main()
