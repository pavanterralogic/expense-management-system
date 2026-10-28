from rest_framework import filters, viewsets
from django.shortcuts import render
from .models import Expense
from .serializers import ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by("-date", "-id")
    serializer_class = ExpenseSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = [
        "description",
        "category",
        "payment_method",
        "notes",
    ]

def expense_page(request):
    return render(request, "expenses/index.html")
