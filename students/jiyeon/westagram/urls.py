from django.urls import path

from users.views import SignupView, LoginView
from postings.views import PostingView
        
urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('posting', PostingView.as_view())
]