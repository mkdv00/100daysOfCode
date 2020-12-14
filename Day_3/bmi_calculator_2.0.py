def main():
    height = float(input("Введите ваш рост в метрах, например, 1.75. - "))
    weight = float(input("Введите ваш вес в киллограммах, например, 60. - "))

    bmi = round(weight / height ** 2)

    if bmi < 18.5:
        print(f"Ваш bmi = {bmi}. У вас слишком маленький вес, для вашего роста.")
    elif bmi < 25:
        print(f"Ваш bmi = {bmi}. У вас нормальный вес, для вашего роста.")
    elif bmi < 30:
        print(f"Ваш bmi = {bmi}. У вас слегка избыточный вес.")
    elif bmi < 35:
        print(f"Ваш bmi = {bmi}. Вы страдаете ожирением.")
    else:
        print(f"Ваш bmi = {bmi}. У вас клиническое ожирение.")


if __name__ == "__main__":
    main()
