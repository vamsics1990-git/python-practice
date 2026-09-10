# Calculate the number of days between two dates in YYYY-MM-DD format.
from datetime import datetime


def calculate_days_in_range(start_date: str, end_date: str) -> int:
    """
    Return the number of days between the start and end dates..

    Args:
        start_date (str): The beginning date in 'YYYY-MM-DD' format.
        end_date (str): The ending date in 'YYYY-MM-DD' format.

    Returns:
        int: The total number of days in the range.

    Raises:
        ValueError: If the start date is later than the end date.
    """
    # Convert the date strings into Python date objects.
    start = datetime.strptime(start_date, "%Y-%m-%d").date()
    end = datetime.strptime(end_date, "%Y-%m-%d").date()

    # Prevent invalid ranges where the starting date is after the ending date.
    if start > end:
        raise ValueError("start_date must be earlier than or equal to end_date.")

    # Compute the full difference in days.
    return (end - start).days


if __name__ == "__main__":
    # Example usage for a sample date range..
    start_date = "2024-01-01"
    end_date = "2024-01-10"
    days = calculate_days_in_range(start_date, end_date)
    print(f"Number of days between {start_date} and {end_date}: {days}")