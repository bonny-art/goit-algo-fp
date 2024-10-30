"""
Основний модуль для запуску програми малювання дерева Піфагора.
"""

import turtle
from tree import draw_tree

def main() -> None:
    """ 
    Налаштовує параметри та запускає малювання дерева.
    """

    branch_length = 200
    angle = 30
    depth = int(input("Введіть рівень рекурсії для дерева: "))

    # Налаштування turtle
    turtle.speed("fastest")
    turtle.left(90)
    turtle.up()
    turtle.goto(0, -300)
    turtle.down()

    # Малюємо дерево
    draw_tree(branch_length, angle, depth)

    # Завершення малювання
    turtle.done()

if __name__ == "__main__":
    main()
