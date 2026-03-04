def get_discounted_prices(prices):
    discounted_prices = []  # Створюємо локальний стан
    
    for price in prices:
        if price > 100:
            new_price = price * 0.8
            discounted_prices.append(new_price) # Мутуємо стан крок за кроком
            
    return discounted_prices

# Викликаємо нашу процедуру
original_prices = [50, 120, 80, 200, 300]
result = get_discounted_prices(original_prices)