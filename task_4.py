from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    date_today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = user_birthday.replace(year=date_today.year)

        if birthday_this_year < date_today:
            birthday_this_year = birthday_this_year.replace(year=date_today.year + 1)

        date_difference = (birthday_this_year - date_today).days

        if 0 <= date_difference <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() >= 5:
                days_to_monday = 7 - congratulation_date.weekday()
                congratulation_date += timedelta(days=days_to_monday)

            formatted_congratulation_date = congratulation_date.strftime("%Y.%m.%d")

            upcoming_birthdays.append({"name": user["name"], "congratulation_date": formatted_congratulation_date})
            
    return upcoming_birthdays

# Example:

users = [{"name": "John Doe", "birthday": "1985.06.18"}, {"name": "Jane Smith", "birthday": "1990.06.21"}]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)