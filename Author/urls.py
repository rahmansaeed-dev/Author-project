from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.forms import PasswordChange, PasswordResetFormView, MySetPasswordForm
from django.contrib.auth import views as auth_views
from app.views import ResetPasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.Register, name='register'),
    path('signin/', views.Sign_in, name='signin'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('buyer/', views.buyer, name='buyer'),
    path('seller/', views.seller, name='seller'),
    path('profile/', views.profile, name='profile'),
    path('showbook/', views.showbook, name='showbook'),
    path('logout/', views.user_logout, name='logout'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    # password reset urls
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),

] 
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


