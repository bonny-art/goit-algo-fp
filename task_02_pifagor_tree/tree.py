"""
Модуль для малювання дерева Піфагора за допомогою рекурсії.
"""

import turtle

def draw_tree(branch_length: float, angle: float, depth: int) -> None:
    """ 
    Малює рекурсивно дерево Піфагора.

    :param branch_length: Довжина гілки.
    :param angle: Кут відхилення гілки.
    :param depth: Глибина рекурсії.
    """

    if depth == 0:
        return

    # Малюємо стовбур/гілку
    turtle.forward(branch_length)

    # Ліва гілка
    turtle.left(angle)
    draw_tree(branch_length * 0.7, angle, depth - 1)

    # Повертаємось до початкового положення для правої гілки
    turtle.right(2 * angle)
    draw_tree(branch_length * 0.7, angle, depth - 1)

    # Повертаємось до початкового кута та положення
    turtle.left(angle)
    turtle.backward(branch_length)
