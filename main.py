from bill_manager import (
    add_bill,
    view_bills,
    update_bill,
    delete_bill
)

from payment_manager import (
    record_payment,
    view_payment_history
)

from report_manager import (
    show_bill_summary,
    show_upcoming_bills,
    show_overdue_bills
)


def main():
    while True:
        print("\n====================================")
        print("     PERSONAL BILL PAYMENT TRACKER")
        print("====================================")

        print("1. Add New Bill")
        print("2. View All Bills")
        print("3. Update Bill")
        print("4. Delete Bill")
        print("5. Record Bill Payment")
        print("6. View Payment History")
        print("7. Bill Summary")
        print("8. Upcoming Bills")
        print("9. Overdue Bills")
        print("10. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_bill()

        elif choice == "2":
            view_bills()

        elif choice == "3":
            update_bill()

        elif choice == "4":
            delete_bill()

        elif choice == "5":
            record_payment()

        elif choice == "6":
            view_payment_history()

        elif choice == "7":
            show_bill_summary()

        elif choice == "8":
            show_upcoming_bills()

        elif choice == "9":
            show_overdue_bills()

        elif choice == "10":
            print("Thank you for using Bill Payment Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
