import turtle

def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3)
            t.left(angle)

def main():
    order = int(input("Введіть рівень рекурсії: "))
    size = 400
    window = turtle.Screen()
    window.bgcolor("white")
    window.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()
    t.color("blue")

    for _ in range(3):
        koch_snowflake(t, order, size)
        t.right(120)

    window.mainloop()

if __name__ == "__main__":
    main()