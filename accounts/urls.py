from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name='login'),
    path("", views.DashboardView.as_view(), name="dashboard"),
]
