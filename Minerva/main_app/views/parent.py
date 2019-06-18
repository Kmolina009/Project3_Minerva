from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from ..forms import ParentSignUpForm
from ..models import Parent, User


class ParentSignUpView(CreateView):
    model = User
    form_class = ParentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'parent'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)

        return redirect('parent_s_index')

# This shows the course index.
def c_index(request):
    return render(request, 'Parents/c_index.html')  

def s_index(request):
    return render(request, 'Parents/s_index.html')

def s_details(request):
    return render(request, 'Parents/s_details.html')
