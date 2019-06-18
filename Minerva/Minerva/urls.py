"""Minerva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from main_app.views import main, student, parent, teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path( '', include('main_app.urls')),
    path('accounts/signup/', main.SignUpView.as_view(), name="signup"),
    path('accounts/signup/Students', student.StudentSignUpView.as_view(), name="student_signup"),
    path('accounts/signup/Teachers/', teacher.TeacherSignUpView.as_view(), name="teacher_signup"),
    path('accounts/signup/Parents/', parent.ParentSignUpView.as_view(), name="parent_signup"),
    ]
