import json

def convert_currency(amount, currency):
    # Задача №1: Добавили GBP (фунт)
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
    amt = float(input("Введите сумму в рублях: "))
    curr = input("Введите целевую валюту (USD, EUR, GBP): ").upper()
    
    result = convert_currency(amt, curr)
    
    # Задача №2: Красивый вывод с разделителями
    print("="*30)
    print("РЕЗУЛЬТАТ КОНВЕРТАЦИИ:")
    print(json.dumps(result, indent=4, ensure_ascii=False))
    print("="*30)

if __name__ == "__main__":
    main()