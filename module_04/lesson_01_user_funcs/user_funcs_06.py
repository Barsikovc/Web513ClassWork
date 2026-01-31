def with_tax(value: (int, float), tax_percentage: float) -> float:
    total = value + value * tax_percentage / 100
    return total


if __name__ == '__main__':
    print(f'Сумма с налогом: {with_tax(10000, 6)}')
    salary = 60000
    income_tax = 13
    print(f'Сумма с налогом: {with_tax(salary, income_tax)}')

