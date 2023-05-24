def calculate_ean13_check_digit(code):
    code_digits = [int(digit) for digit in code]
    odd_digits = code_digits[::2]
    even_digits = code_digits[1::2]
    odd_sum = sum(odd_digits)
    even_sum = sum(even_digits)
    total = odd_sum + even_sum * 3
    check_digit = (10 - (total % 10)) % 10
    return check_digit


while True:
    ean_code = input("Введите код EAN-13 (без контрольной цифры): ")

    if len(ean_code) != 12 or not ean_code.isdigit():
        print("Ошибка: Введен неверный формат кода.")
        continue

    try:
        check_digit = calculate_ean13_check_digit(ean_code)
        ean13_code = ean_code + str(check_digit)
        break
    except Exception as e:
        print("Ошибка при расчете контрольной цифры:", str(e))

print("Контрольная цифра EAN-13:", check_digit)
print("Полный номер EAN-13:", ean13_code)
