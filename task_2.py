import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min >= 1 and max <= 1000 and min <=max and quantity > 0 and quantity <= (max - min + 1):
        list_of_unique_lottery_numbers = random.sample(range(min, max + 1), quantity)
        list_of_unique_lottery_numbers.sort()
        return list_of_unique_lottery_numbers
    else:
        return []
    
# Example:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)