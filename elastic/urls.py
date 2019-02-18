from django.urls import path

from .views import index

app_name='elastic'

urlpatterns = [
    # as_view() 클래스 함수 호출(entry point)
    path('', index.as_view(), name='index'),
]