import tkinter as tk


# Функция для движения мяча
def move_ball():
    global y, vy, radius, ground, canvas, gravity, bounces, max_bounces, elasticity, running

    if running:
        # Проверяем столкновение с землей
        if y + vy + radius >= ground:
            vy *= -elasticity  # Учет упругости при отскоке
            bounces += 1  # Увеличиваем счетчик отскоков

            # Останавливаем мяч, если он достиг максимального количества отскоков и опустился ниже земли
            if bounces >= max_bounces and y + vy + radius >= ground:
                vy = 0
                running = False

        # Уменьшаем скорость мяча под воздействием гравитации
        vy += gravity  # Учитываем гравитацию

        # Обновляем позицию
        y += vy  # Движение по оси Y

        # Очищаем Canvas и рисуем мяч в новом положении
        canvas.delete("all")
        canvas.create_oval(200 - radius, y - radius, 200 + radius, y + radius, fill="red")  # Рисуем мяч

        # Если мяч все еще движется и не достиг максимального числа отскоков, вызываем функцию снова через dt миллисекунд
        if running and (bounces < max_bounces or vy != 0):
            root.after(10, move_ball)


# Функция для применения значений силы притяжения и упругости мяча
def apply_values():
    global gravity, elasticity
    gravity = float(gravity_entry.get())
    elasticity = float(elasticity_entry.get())


# Функция для запуска движения мяча
def start():
    global running
    running = True
    move_ball()
    start_button.grid_forget()  # Скрываем кнопку "Начать"
    apply_button.grid_forget()  # Скрываем кнопку "Применить"
    gravity_label.grid_forget()  # Скрываем метку для силы притяжения
    gravity_entry.grid_forget()  # Скрываем поле ввода для силы притяжения
    elasticity_label.grid_forget()  # Скрываем метку для упругости мяча
    elasticity_entry.grid_forget()  # Скрываем поле ввода для упругости мяча


# Создание окна
root = tk.Tk()
root.title("Упругое столкновение мяча с землей")

# Создание Canvas (холста) для отрисовки
canvas = tk.Canvas(root, width=400, height=400)
canvas.grid(row=0, column=0, columnspan=2)

# Параметры мяча и земли
y = 50  # Начальная позиция мяча по оси Y
vy = 1.0  # Начальная скорость мяча по оси Y
radius = 20  # Радиус мяча
ground = 380  # Позиция земли
gravity = 0.1  # Ускорение свободного падения
bounces = 0  # Счетчик отскоков
max_bounces = 3  # Максимальное количество отскоков
elasticity = 0.9  # Упругость мяча
running = False  # Переменная для управления движением мяча

# Отрисовка мяча в начальной позиции
canvas.create_oval(200 - radius, y - radius, 200 + radius, y + radius, fill="red")

# Поле ввода для силы притяжения земли
gravity_label = tk.Label(root, text="Сила притяжения земли:")
gravity_label.grid(row=1, column=0, padx=5, pady=5)
gravity_entry = tk.Entry(root)
gravity_entry.grid(row=1, column=1, padx=5, pady=5)
gravity_entry.insert(0, str(gravity))

# Поле ввода для упругости мяча
elasticity_label = tk.Label(root, text="Упругость мяча:")
elasticity_label.grid(row=2, column=0, padx=5, pady=5)
elasticity_entry = tk.Entry(root)
elasticity_entry.grid(row=2, column=1, padx=5, pady=5)
elasticity_entry.insert(0, str(elasticity))

# Кнопка "Применить" для обновления значений силы притяжения и упругости мяча
apply_button = tk.Button(root, text="Применить", command=apply_values, bg="lightblue")
apply_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Кнопка для начала движения мяча
start_button = tk.Button(root, text="Начать", command=start, bg="lightgreen")
start_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='ew')

# Запуск основного цикла
root.mainloop()
