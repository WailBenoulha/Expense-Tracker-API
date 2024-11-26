from django.contrib import admin
from .models import CustomUser,Expenses,Incomes

admin.site.register(CustomUser)
admin.site.register(Expenses)
admin.site.register(Incomes)