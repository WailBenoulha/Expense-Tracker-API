from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet,IncomesViewSet,TotalCoast,CostInThreeMonth

router = DefaultRouter()
router.register('expenses',ExpenseViewSet,basename='expenses')
router.register('incomes',IncomesViewSet,basename='incomes')
router.register('totalcoast',TotalCoast,basename='costs')
router.register('cost_in_3_Months',CostInThreeMonth,basename='costthreemonth')
app_name = 'expenses'

urlpatterns = [
    path('',include(router.urls)),
]