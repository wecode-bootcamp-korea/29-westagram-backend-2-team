from django.urls import path

from users.views import SignupView, LoginView
from postings.views import PostingView, CommentView
        
urlpatterns = [
    path('signup', SignupView.as_view()),
    path('login', LoginView.as_view()),
    path('posting', PostingView.as_view()),
    path('comment', CommentView.as_view())
]