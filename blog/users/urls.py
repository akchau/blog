from django.contrib.auth.views import LogoutView, LoginView, PasswordChangeDoneView, PasswordChangeView, PasswordResetView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    # этой страницы по соображениям безопасности нет Регистрация
    path('signup/', views.SignUp.as_view(template_name='users/signup.html'), name='signup'),
    # Авторизация
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'), 

    # Выход
    path('logout/', LogoutView.as_view(template_name='users/logged_out.html'), name='logout'), 

    # Смена пароля
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html'), name='password_change'),

    # Сообщение об успешном изменении пароля
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),

    # Восстановление пароля
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'), name='password_reset'),

    # Сообщение об отправке ссылки для восстановления пароля
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),

    # Вход по ссылке для восстановления пароля
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),

    # Сообщение об успешном восстановлении пароля
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),

    path('cabinet/<slug:username>/', views.cabinet, name='cabinet'), 
    path('feedback/', views.feedback, name='feedback'),
] 