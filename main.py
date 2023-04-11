if __name__ == '__main__':
    money = float(input("Введите сумму депозита: "))
    per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
    deposit = {}
    for bank, percent in per_cent.items():
        deposit[bank] = money * (percent/100)
    print("Максимальная сумма, которую вы можете заработать - " + str(round(max(deposit.values()), 3)))
