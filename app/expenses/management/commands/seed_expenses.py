from datetime import date

from django.core.management.base import BaseCommand

from expenses.models import Expense


class Command(BaseCommand):
    help = "Create sample expense records"


    def handle(self, *args, **options):

        expenses = [
            {
                "description": "Office Lunch",
                "category": "Food",
                "amount": 450.00,
                "date": date(2026, 10, 1),
                "payment_method": "UPI",
                "notes": "Team lunch",
            },
            {
                "description": "Cab Travel",
                "category": "Travel",
                "amount": 850.00,
                "date": date(2026, 10, 2),
                "payment_method": "Credit Card",
                "notes": "Office travel",
            },
            {
                "description": "Internet Bill",
                "category": "Utilities",
                "amount": 1200.00,
                "date": date(2026, 10, 3),
                "payment_method": "UPI",
                "notes": "Monthly internet bill",
            },
        ]


        for expense_data in expenses:

            Expense.objects.get_or_create(
                description=expense_data["description"],
                date=expense_data["date"],
                defaults=expense_data,
            )


        self.stdout.write(
            self.style.SUCCESS(
                "Sample expenses created successfully."
            )
        )
