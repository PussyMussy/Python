def parse_domain(domain):
    # Разделение доменного имени на отдельные части
    parts = domain.split('.')
    # Вывод доменных частей в обратном порядке
    for i in range(len(parts) - 1, -1, -1):
        print(parts[i])

# Ввод доменного имени
domain_name = input("Введите доменное имя сайта: ")

# Вызов функции и вывод результата
parse_domain(domain_name)
