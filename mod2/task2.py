def calculate_square(side_length):
    perimeter = 4 * side_length
    area = side_length ** 2
    diagonal = (2 ** 0.5) * side_length  # Формула для диагонали квадрата
    return round(perimeter, 2), round(area, 2), round(diagonal, 2)

side_lengths = input("Введите длины сторон квадрата через пробел: ").split()
for side_length in side_lengths:
    side_length = float(side_length)
    perimeter, area, diagonal = calculate_square(side_length)
    print("Длина стороны квадрата:", side_length)
    print("Периметр квадрата:", perimeter)
    print("Площадь квадрата:", area)
    print("Диагональ квадрата:", diagonal)