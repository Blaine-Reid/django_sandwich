from django.urls import path,include
from sandwich_app.views import IndexView, SandwichView, IngrediantView, RandomView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sandwich/', SandwichView.as_view(), name='sandwich'),
    path('sandwich/random/', RandomView.as_view(), name='random'),
    path('sandwich/<str:ingrediant>', IngrediantView.as_view(), name='ingrediant'),
]


