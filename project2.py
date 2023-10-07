n = int(input("Введіть кількість рядків: "))

s = []

for i in range(n):
    s2 = input(f"Введіть рядок {i+1} (парна довжина, літери): ")
    s.append(s2)

def transform_s2(s2):
    middle = len(s2) // 2
    first_half = s2[:middle]
    second_half = s2[middle:]
    transformed_s2 = first_half + second_half.upper()
    return transformed_s2

for s2 in s:
    transformed_s2 = transform_s2(s2)
    print(transformed_s2)

