from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from . import views


app_name = 'core'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
