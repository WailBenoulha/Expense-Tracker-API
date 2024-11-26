from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet,IncomesViewSet

router = DefaultRouter()
router.register('expenses',ExpenseViewSet)
router.register('incomes',IncomesViewSet)
app_name = 'expenses'

urlpatterns = [
    path('',include(router.urls)),
]