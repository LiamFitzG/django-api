from django.contrib import admin
from django.urls import path
from user_api.views import user_all, user_id

urlpatterns = [
    path('', user_all),
    path('<int:id>', user_id)
]