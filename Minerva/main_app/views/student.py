from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import StudentSignUpForm
from ..models import Student, User

class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name='registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_ass_index')


def ass_index(request):
    return render(request, 'Students/ass_index.html')

def ass_details(request):
    return render(request, 'Students/ass_details.html')

def completed_index(request):
    return render(request, 'Students/Completed.html')

def course_index(request):
    return render(request, 'Students/course_index.html')
