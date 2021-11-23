from django.contrib import admin
from django.urls import path
from tracking_api.views import ListCryptocurrencyView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('cryptocurrency/', ListCryptocurrencyView.as_view()),
]
