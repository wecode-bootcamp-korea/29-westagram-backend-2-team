from django.urls import path

 urlpatterns = [
 path('/login', UserView.as_view()),
      '/loginview', LoginView.as_view()
 ]

 
