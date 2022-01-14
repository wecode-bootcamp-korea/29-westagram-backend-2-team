from django.urls   import path
from .views   import UserView

urlpatterns = [
    path('/userview',UserView.as_view()),
]
