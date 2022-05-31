from django.shortcuts import redirect
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

from .views import ProfileView


app_name = 'core'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('accounts/profile/', ProfileView.as_view(template_name='login/profile.html'), name='profile'),
    path('accounts/', RedirectView.as_view(url="/accounts/profile/"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
