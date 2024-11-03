from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class DashboardView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'


class LogoutView(auth_views.LogoutView):
    pass
