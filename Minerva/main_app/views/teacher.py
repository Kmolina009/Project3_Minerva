from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import TeacherSignUpForm
from ..models import Teacher, User


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('teacher_class_index')

def ass_assign(request):
    return render(request, 'Teachers/ass_assign.html')

def classroom_index(request):
    return render(request, 'Teachers/classroom_index.html')

def classroom_s_index(request):
    return render(request, "Teachers/classroom_s_index.html")

def s_details(request):
    return render(request, 'Teachers/s_details.html')
