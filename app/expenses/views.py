from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpensesSerializer,IncomesSerializer
from core.models import Expenses,Incomes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum
from rest_framework.exceptions import ValidationError

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)    


class IncomesViewSet(viewsets.ModelViewSet):
    serializer_class = IncomesSerializer
    queryset = Incomes.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)    

from datetime import date,timedelta

class CostView(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        enddate = date.today()
        startdate1 = enddate - timedelta(days=30)
        startdate2 = enddate - timedelta(days=90)
        # expenses total
        total_expense = Expenses.objects.all().filter(user=self.request.user).aggregate(
            total = Sum('coast')
        )['total'] or 0
        # incomes total
        total_incomes = Incomes.objects.filter(user=self.request.user).aggregate(
            total = Sum('coast')
        )['total'] or 0
        # expenses in one month
        instance1 = Expenses.objects.filter(
            user=self.request.user,
            date__range = [startdate1,enddate]
        ).aggregate(total=Sum('coast'))['total'] or 0
        # incomes in one month
        instance3 = Incomes.objects.filter(
            user=self.request.user,
            date__range = [startdate1,enddate]
        ).aggregate(total=Sum('coast'))['total'] or 0
        # expense in 3 months
        instance2 = Expenses.objects.filter(
            date__range = [startdate2,enddate],
            user=self.request.user,
        ).aggregate(total=Sum('coast'))['total'] or 0
        # incomes in 3 months
        instance4 = Incomes.objects.filter(
            user=self.request.user,
            date__range = [startdate2,enddate],
        ).aggregate(total=Sum('coast'))['total'] or 0
        # Net profit/loss
        instance5 = total_incomes - total_expense
        instance6 = instance3 - instance1
        instance7 = instance4 - instance2
        return Response({
            'Total expenses':total_expense,
            'Total incomes':total_incomes,
            'expenses in 1 month':instance1,
            'incomes in 1 month':instance3,
            'expenses in 3 months':instance2,
            'incomes in 3 months':instance4,
            'Total Net income':instance5,
            'Total Net income in 1 month':instance6,
            'Total Net income in 3 months':instance7,
        })   