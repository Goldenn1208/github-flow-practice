import json

def convert_currency(amount, currency):
    rates = {"USD": 92.5, "EUR": 100.2, "GBP": 115.7}
    
    if currency not in rates:
        return {"error": "Валюта не поддерживается"}
    
    converted = round(amount / rates[currency], 2)
    return {
        "initial_amount": amount,
        "currency": currency,
        "converted_amount": converted
    }

def main():
    print("=== МИКРОСЕРВИС КОНВЕРТАЦИИ ===")
    
    # Задача №3: Валидация (чтобы не падало от букв)
    try:
        amt = float(input("Введите сумму в рублях: "))
    except ValueError:
        print("="*30)
        print("ОШИБКА: Введите числовое значение!")
        print("="*30)
        return

    curr = input("Введите целевую валюту (USD, EUR, GBP): ").upper()
    
    result = convert_currency(amt, curr)
    
    print("="*30)
    print("РЕЗУЛЬТАТ ОПЕРАЦИИ:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
    print("="*30)

if __name__ == "__main__":
    main()