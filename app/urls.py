from django.urls import path
import app.views as app_vievs


urlpatterns = [
    path('', app_vievs.product_list, name = 'product_list'),
    path('<str:product_name>/', app_vievs.product_info, name = 'product_info'),
    path('Product/<str:product_name>/review/', app_vievs.user_response, name='user_response'),
    ]