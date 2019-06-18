from django.contrib import admin
from .models import User, Student, Teacher, Parent, Courses, Assignment, Classroom

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Courses)
admin.site.register(Assignment)
admin.site.register(Classroom)

