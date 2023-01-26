from django.urls import path

from mainapp import views


urlpatterns = [
    path("", views.HelloWorldView.as_view()),
    path("<str:word>/", views.check_kwargs),
]
