from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet,IncomesViewSet,CostView

router = DefaultRouter()
router.register('expenses',ExpenseViewSet,basename='expenses')
router.register('incomes',IncomesViewSet,basename='incomes')
router.register('costs',CostView,basename='costs')
app_name = 'expense'

urlpatterns = [
    path('',include(router.urls)),
]