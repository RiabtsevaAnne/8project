s = input("Введіть рядок слів: ")

words = s.split()

s2 = len(words)

s3 = max(words, key=len)

print("Кількість слів:", s2)
print("Найдовше слово:", s3)
