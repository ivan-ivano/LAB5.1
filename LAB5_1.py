def h(x, y):
    return x * y / (1 + x ** 2 * y ** 2)


s = 2
t = 3

result = (h(s ** 2, t ** 2) + (h(s + t, 1) ** 2)) / (1 + h(s * t, 2) ** 2)

print("Результат:", result)
