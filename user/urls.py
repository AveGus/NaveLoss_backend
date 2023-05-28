from django.urls import path, include

from user.views import UserByToken

urlpatterns = [
    path('by/Token', UserByToken.as_view())
]