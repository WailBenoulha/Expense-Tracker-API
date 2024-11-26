from rest_framework import viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpensesSerializer,IncomesSerializer
from core.models import Expenses,Incomes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum

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

    # def total_in_month(self):
    #     for exp in Expenses:   
    #         if exp['date']

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

class TotalCoast(viewsets.ViewSet):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self,request):
        total_coast = Expenses.objects.all().aggregate(
            total = Sum('coast')
        )['total'] or 0
        return Response({
            'Total_coast':total_coast,
        })
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id') 
 
from datetime import date,timedelta

class CostInThreeMonth(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def list(self,request):
        enddate = date.today()
        startdate = enddate - timedelta(days=90)
        instance = Expenses.objects.filter(
            date__range = [startdate,enddate]
        ).aggregate(total=Sum('coast'))['total'] or 0
        return Response({'cost in 3 months':instance})
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    
   