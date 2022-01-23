from django.urls import path

from .views import CategoryView
from .views import ProductView
from .views import BotUserView
from .views import SubCategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    # path('sub-categories/', SubCategoryView.as_view(), name='sub-categories'),
    path('products/', ProductView.as_view(), name='products'),
    path('bot-users/', BotUserView.as_view(), name='bot_users'),
]
