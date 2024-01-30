from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
      path('', views.index, name='index'), # manga/
      path('<int:book_id>/', views.show, name='show'), # manga/<id>
      path('addBook/', views.add, name='add'), # manga/add
      path('editBook/', views.edit, name='edit'), # manga/edit
      path('deleteBook/', views.remove, name='delete'), # manga/edit
]