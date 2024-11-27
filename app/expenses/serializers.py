from rest_framework import serializers
from core.models import Expenses,Incomes


class ExpensesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expenses
        fields = ['id','coast','date','category']
        read_only_fields = ['id']

class IncomesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incomes
        fields = ['id','coast','date']
        read_only_fields = ['id']        