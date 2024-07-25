import heapq

def min_cost_to_connect_cables(cables):
    # Створюємо мін-купу з початкових довжин кабелів
    heapq.heapify(cables)
    
    total_cost = 0

    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Виймаємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання цих кабелів
        cost = first + second
        
        # Додаємо вартість до загальної суми
        total_cost += cost
        
        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, cost)
        
        # Виводимо проміжні кроки
        print(f"З'єднуємо {first} і {second}, вартість: {cost}, загальні витрати: {total_cost}, купа: {cables}")
    
    return total_cost

# тестовий приклад

if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    cables1 = [1, 2, 3, 4, 5]
    cables2 = [4, 3, 2, 6]
    cables3 = [1, 2, 3]
    print(f"Мінімальна вартість з'єднання кабелів {cables}: {min_cost_to_connect_cables(cables)}") 
    print(f"Мінімальна вартість з'єднання кабелів {cables1}: {min_cost_to_connect_cables(cables1)}")
    print(f"Мінімальна вартість з'єднання кабелів {cables2}: {min_cost_to_connect_cables(cables2)}")
    print(f"Мінімальна вартість з'єднання кабелів {cables3}: {min_cost_to_connect_cables(cables3)}")