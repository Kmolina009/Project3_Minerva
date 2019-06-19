from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from ..forms import LoginForm

class SignUpView(TemplateView):
    template_name = 'Registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacher_class_index')
        elif request.user.is_student:
            return redirect('student_ass_index')
        else:
            return redirect('parent_s_index')
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        next = request.POST.get('next') or None
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and next is not None:
                login(request, user)
                return redirect(next)
            elif user is not None and next is None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Sorry, your username or password was invalid'
    form = LoginForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'Registration/login_view.html', context)


def logout_view(request):
    logout(request)
    return redirect('home')


