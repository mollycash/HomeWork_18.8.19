def calculate_ticket_cost(num_tickets):
    total_cost = 0

    for i in range(num_tickets):
        age = int(input(f"Введите возраст посетителя {i + 1}: "))

        if age < 18:
            ticket_cost = 0  # Бесплатно для посетителей младше 18 лет
        elif 18 <= age < 25:
            ticket_cost = 990  # Стоимость 990 рублей для посетителей от 18 до 25 лет
        else:
            ticket_cost = 1390  # Полная стоимость 1390 рублей для посетителей от 25 лет и старше

        total_cost += ticket_cost

    # Применение скидки 10% для заказов более трех билетов
    if num_tickets > 3:
        total_cost *= 0.9

    return total_cost


def main():
    try:
        num_tickets = int(input("Введите количество билетов: "))
        if num_tickets <= 0:
            print("Количество билетов должно быть положительным числом.")
            return

        total_cost = calculate_ticket_cost(num_tickets)
        print(f"Сумма к оплате: {total_cost} руб.")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")


if __name__ == "__main__":
    main()
