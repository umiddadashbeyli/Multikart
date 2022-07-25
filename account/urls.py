from django.urls import path, reverse_lazy
from . import views 
from django.contrib.auth import views as auth_views
from account.views import CustomLoginView, RegistrationView, ActiveAccountView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('change/', views.change, name='change'),
    # path('change/', 
    #     auth_views.PasswordChangeView.as_view(
    #         template_name='change_pwd.html',
    #         success_url = reverse_lazy('change_done'),
    #         form_class = MyChangeFormPassword,
    #     ), 
    #         name='change'),
    path('change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='change_pwd_done.html'), name='change_done'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<str:uidb64>/<str:token>/', ActiveAccountView.as_view() , name='activate'),
]