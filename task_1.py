from datetime import datetime

def get_days_from_today(date: str) -> int | None:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        date_today = datetime.today().date()
        days_difference = (date_today - input_date).days
        return days_difference
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return None
    
# Example:
print(get_days_from_today("2025-06-25"))