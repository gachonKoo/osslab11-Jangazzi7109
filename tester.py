from geo.utils import to_float, circle_area

def main():
    c = to_float(5)
    area = circle_area(10)   # π * 10^2 = 314.1592653589793

    print(f"c = {c}")
    print(f"area = {area}")

if __name__ == "__main__":
    main()
