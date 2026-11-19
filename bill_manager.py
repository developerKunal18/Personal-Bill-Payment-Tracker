from config import BILLS_FILE
from storage import load_data, save_data
from utils import (
    get_next_id,
    get_valid_amount,
    get_valid_date,
    print_line
)


def add_bill():
    bills = load_data(BILLS_FILE)

    name = input("Enter bill name: ").strip()
    category = input(
        "Enter category (Electricity/Internet/Rent/Mobile/Other): "
    ).strip()

    if not name or not category:
        print("Bill name and category are required.")
        return

    amount = get_valid_amount("Enter bill amount: ₹")
    due_date = get_valid_date("Enter due date (YYYY-MM-DD): ")

    bill = {
        "id": get_next_id(bills),
        "name": name,
        "category": category,
        "amount": amount,
        "due_date": due_date,
        "status": "Unpaid"
    }

    bills.append(bill)
    save_data(BILLS_FILE, bills)

    print("Bill added successfully!")


def view_bills():
    bills = load_data(BILLS_FILE)

    print_line()
    print("ALL BILLS")
    print_line()

    if not bills:
        print("No bills found.")
        return

    for bill in sorted(bills, key=lambda item: item["due_date"]):
        print(f"ID: {bill['id']}")
        print(f"Name: {bill['name']}")
        print(f"Category: {bill['category']}")
        print(f"Amount: ₹{bill['amount']:.2f}")
        print(f"Due Date: {bill['due_date']}")
        print(f"Status: {bill['status']}")
        print_line()


def update_bill():
    bills = load_data(BILLS_FILE)

    try:
        bill_id = int(input("Enter bill ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for bill in bills:
        if bill["id"] == bill_id:
            name = input(
                f"New name [{bill['name']}]: "
            ).strip()

            category = input(
                f"New category [{bill['category']}]: "
            ).strip()

            amount = input(
                f"New amount [{bill['amount']}]: "
            ).strip()

            due_date = input(
                f"New due date [{bill['due_date']}]: "
            ).strip()

            if name:
                bill["name"] = name

            if category:
                bill["category"] = category

            if amount:
                try:
                    new_amount = float(amount)

                    if new_amount <= 0:
                        print("Amount must be greater than zero.")
                        return

                    bill["amount"] = round(new_amount, 2)

                except ValueError:
                    print("Invalid amount.")
                    return

            if due_date:
                try:
                    bill["due_date"] = (
                        get_date_without_prompt(due_date)
                    )
                except ValueError:
                    print("Invalid date. Use YYYY-MM-DD.")
                    return

            save_data(BILLS_FILE, bills)
            print("Bill updated successfully!")
            return

    print("Bill not found.")


def get_date_without_prompt(value):
    from datetime import date
    return date.fromisoformat(value).isoformat()


def delete_bill():
    bills = load_data(BILLS_FILE)

    try:
        bill_id = int(input("Enter bill ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    bill = next(
        (item for item in bills if item["id"] == bill_id),
        None
    )

    if not bill:
        print("Bill not found.")
        return

    confirm = input(
        f"Delete '{bill['name']}' and its payment history? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("Deletion cancelled.")
        return

    updated_bills = [
        item for item in bills
        if item["id"] != bill_id
    ]

    from config import PAYMENTS_FILE

    payments = load_data(PAYMENTS_FILE)

    updated_payments = [
        payment for payment in payments
        if payment["bill_id"] != bill_id
    ]

    save_data(BILLS_FILE, updated_bills)
    save_data(PAYMENTS_FILE, updated_payments)

    print("Bill and payment history deleted.")
