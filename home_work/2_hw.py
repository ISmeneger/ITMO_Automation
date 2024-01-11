# Задача 1
def task_1():
    a: int = 10
    b: float = 5.25
    c: str = 'Тестировщик'
    d: list = [1, 2, 3]
    f: bool = True
    print(type(a), type(b), type(c), type(d), type(f), '\n')
task_1()
# Задача 2
def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21]
    return a[:3]
print(task_2(), '\n')
# Поcледовательность чисел называется элементами списка
# Задача 3
def task_3(a: int) -> int:
    return a ** 2
print(task_3(9))