from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


# Create your views here.
class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class SubCategoryView(APIView):
    def get(self, request):
        subcategories = SubCategory.objects.all()
        category_id = request.GET.get('category_id')
        if category_id:
            subcategories = subcategories.filter(category__id=category_id)
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        category_id = request.GET.get('category_id')
        if category_id:
            products = products.filter(category__id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class BotUserView(APIView):
    def get(self, request):
        users = BotUser.objects.all()
        serializer = BotUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BotUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

#
# @api_view(['GET'])
# # select one user by params
# def get_user(self, request):  # params: could be telegram_id or username
#     try:
#         user = BotUser.objects.get(**request.query_params)
#     except BotUser.DoesNotExist:
#         user = None


# def get_user(self, user_id):
#     try:
#         user = BotUser.objects.get(id=user_id)
#     except BotUser.DoesNotExist:
#         user = None
#
#     if user is not None:
#         serializer = BotUserSerializer(user)
#         return Response(serializer.data)
#     else:
#         return Response({"error": "User not found"})
