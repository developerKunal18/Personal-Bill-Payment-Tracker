from datetime import date, timedelta

from config import BILLS_FILE
from storage import load_data
from utils import print_line


def show_bill_summary():
    bills = load_data(BILLS_FILE)

    if not bills:
        print("No bills available.")
        return

    paid = [
        bill for bill in bills
        if bill["status"] == "Paid"
    ]

    unpaid = [
        bill for bill in bills
        if bill["status"] == "Unpaid"
    ]

    paid_total = sum(bill["amount"] for bill in paid)
    unpaid_total = sum(bill["amount"] for bill in unpaid)

    print_line()
    print("BILL SUMMARY")
    print_line()

    print(f"Total bills: {len(bills)}")
    print(f"Paid bills: {len(paid)}")
    print(f"Unpaid bills: {len(unpaid)}")
    print(f"Total paid: ₹{paid_total:.2f}")
    print(f"Total pending: ₹{unpaid_total:.2f}")
    print(f"Total bill amount: ₹{paid_total + unpaid_total:.2f}")


def show_upcoming_bills():
    bills = load_data(BILLS_FILE)

    today = date.today()
    last_date = today + timedelta(days=7)

    upcoming = [
        bill for bill in bills
        if bill["status"] == "Unpaid"
        and today <= date.fromisoformat(bill["due_date"]) <= last_date
    ]

    print_line()
    print("UPCOMING BILLS - NEXT 7 DAYS")
    print_line()

    if not upcoming:
        print("No upcoming unpaid bills.")
        return

    for bill in sorted(upcoming, key=lambda item: item["due_date"]):
        print(
            f"{bill['name']} | "
            f"₹{bill['amount']:.2f} | "
            f"Due: {bill['due_date']}"
        )


def show_overdue_bills():
    bills = load_data(BILLS_FILE)
    today = date.today()

    overdue = [
        bill for bill in bills
        if bill["status"] == "Unpaid"
        and date.fromisoformat(bill["due_date"]) < today
    ]

    print_line()
    print("OVERDUE BILLS")
    print_line()

    if not overdue:
        print("No overdue bills.")
        return

    for bill in sorted(overdue, key=lambda item: item["due_date"]):
        print(
            f"{bill['name']} | "
            f"₹{bill['amount']:.2f} | "
            f"Due: {bill['due_date']}"
        )
