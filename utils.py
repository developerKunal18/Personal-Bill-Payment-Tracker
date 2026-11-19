from datetime import date


def get_next_id(records):
    if not records:
        return 1

    return max(record["id"] for record in records) + 1


def get_valid_amount(message):
    while True:
        try:
            amount = float(input(message))

            if amount <= 0:
                print("Amount must be greater than zero.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Enter a valid amount.")


def get_valid_date(message):
    while True:
        value = input(message).strip()

        try:
            return date.fromisoformat(value).isoformat()
        except ValueError:
            print("Enter date in YYYY-MM-DD format.")


def print_line():
    print("-" * 60)
