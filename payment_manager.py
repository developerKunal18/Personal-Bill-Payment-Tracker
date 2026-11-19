from config import BILLS_FILE, PAYMENTS_FILE
from storage import load_data, save_data
from utils import get_next_id, get_valid_date, print_line


def record_payment():
    bills = load_data(BILLS_FILE)
    payments = load_data(PAYMENTS_FILE)

    unpaid_bills = [
        bill for bill in bills
        if bill["status"] == "Unpaid"
    ]

    if not unpaid_bills:
        print("No unpaid bills available.")
        return

    print("\nUNPAID BILLS")
    print_line()

    for bill in unpaid_bills:
        print(
            f"ID: {bill['id']} | "
            f"{bill['name']} | "
            f"₹{bill['amount']:.2f} | "
            f"Due: {bill['due_date']}"
        )

    try:
        bill_id = int(input("\nEnter bill ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    bill = next(
        (
            item for item in bills
            if item["id"] == bill_id
            and item["status"] == "Unpaid"
        ),
        None
    )

    if not bill:
        print("Unpaid bill not found.")
        return

    payment_date = get_valid_date(
        "Enter payment date (YYYY-MM-DD): "
    )

    payment = {
        "id": get_next_id(payments),
        "bill_id": bill_id,
        "amount": bill["amount"],
        "payment_date": payment_date
    }

    payments.append(payment)
    bill["status"] = "Paid"

    save_data(PAYMENTS_FILE, payments)
    save_data(BILLS_FILE, bills)

    print("Payment recorded successfully!")
    print(f"Paid amount: ₹{bill['amount']:.2f}")


def view_payment_history():
    payments = load_data(PAYMENTS_FILE)
    bills = load_data(BILLS_FILE)

    print_line()
    print("PAYMENT HISTORY")
    print_line()

    if not payments:
        print("No payment records found.")
        return

    bill_map = {
        bill["id"]: bill["name"]
        for bill in bills
    }

    for payment in sorted(
        payments,
        key=lambda item: (item["payment_date"], item["id"])
    ):
        name = bill_map.get(
            payment["bill_id"],
            "Deleted bill"
        )

        print(
            f"Payment ID: {payment['id']} | "
            f"Bill: {name} | "
            f"Amount: ₹{payment['amount']:.2f} | "
            f"Date: {payment['payment_date']}"
        )
