from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
      path('', views.index, name='index'), # manga/
      path('<int:book_id>/', views.show, name='show')

]