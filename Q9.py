# Q9:

def days_since_birthday(birthday):
    """
    Calculates the days passed since birthdate excluding birth year and current year.
    :param birthday: In "DD-MM-YYYY" format
    :return: Number of days passed (excluding birth year and current year)
    """

    birth_year = int(birthday.split("-")[-1])
    current_year = 2025

    # Count the number of whole years
    full_years = current_year - birth_year - 1

    # Each full year contributes 365 days (not measuring leap years)
    days_passed = full_years * 365

    return days_passed