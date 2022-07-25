from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from core.forms import SubscriberForm
from account.forms import RegisterForm, LoginForm, ChangePasswordForm
from django.contrib.auth import login as django_login, authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View
from django.contrib.sites.shortcuts import get_current_site


from account.tasks import send_confirmation_mail
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from account.tokens import account_activation_token


User = get_user_model()


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class  = LoginForm
    success_url = reverse_lazy('home')


class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


    def form_valid(self, form):
        result = super().form_valid(form)
        send_confirmation_mail(user=self.object, current_site=get_current_site(self.request))
        return result

class ActiveAccountView(View):

    def get(self, request, *args, **kwargs):
        uidb64 = kwargs['uidb64']
        token = kwargs['token']
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(request, 'Your account activated!')
            return redirect(reverse_lazy('login'))
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect(reverse_lazy('login'))
        





def change (request):
    next_page = request.GET.get('next')
    form = ChangePasswordForm()
    form1 = SubscriberForm()
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST)
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
        elif form.is_valid():
            oldpassword = form.cleaned_data.get("oldpassword")
            if not request.user.check_password(oldpassword):
                messages.error(request,'Old password is not True')
                return redirect(reverse_lazy('change'))
            newpassword = form.cleaned_data.get("newpassword2")
            request.user.set_password(newpassword)   
            request.user.save()
            if next_page:
                return redirect(next_page)
            return redirect(reverse_lazy('change_done'))
    context = {
        'form' : form,
        'form1' : form1
    }
    return render(request, 'change_pwd.html', context)
    
# def login (request):
#     next_page = request.GET.get('next', reverse_lazy('home'))
#     form1 = SubscriberForm()
#     form = LoginForm()
#     if request.method == 'POST':
#         form1 = SubscriberForm(data = request.POST)
#         form = LoginForm(data = request.POST)
#         if form.is_valid():
#             user = authenticate(request,  username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#             if user is not None:
#                 django_login(request, user)
#                 return redirect(next_page)
                
#         elif form1.is_valid():
#             form1.save()
#             return redirect(reverse_lazy('home'))
#     context = {
#         'form1' : form1,
#         'form' : form
#     }
#     return render(request, 'login.html', context)


# def logout(request):
#     django_logout(request)
#     return redirect(reverse_lazy('login'))


@login_required
def profile (request):
    form1 = SubscriberForm()
    if request.method == 'POST':
        form1 = SubscriberForm(data = request.POST)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('home'))
    context = {
        'form' : form1,
        'user' : request.user
    }
    return render(request, 'profile.html', context)



# def register (request):
#     form = RegisterForm()
#     form1 = SubscriberForm()
#     if request.method == 'POST':
#         form = RegisterForm(data = request.POST)
#         form1 = SubscriberForm(data = request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse_lazy('login'))
#         elif form1.is_valid():
#             form1.save()
#             return redirect(reverse_lazy('home'))
#         else:
#             form = RegisterForm()
#     context = {
#         'form' : form,
#         'form1' : form1,
#     }
#     return render(request, 'register.html', context)
