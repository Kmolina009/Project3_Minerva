from django.urls import path 
from .views import teacher, student, parent, main

urlpatterns = [
    path('', main.home, name='home'),

    path('Students/home/', student.login, name='student_login'),
    path('Students/ass_index/', student.ass_index, name='student_ass_index'),
    path('Students/ass_details/', student.ass_details, name='student_ass_details'),
    path('Students/course_index/', student.course_index, name='student_course_index'),
    path('Students/comp_index/', student.completed_index, name='student_comp_index'),

    path('Teachers/home/', teacher.login, name='teacher_login'),
    path('Teachers/class_index/', teacher.classroom_index, name='teacher_class_index'),
    path('Teachers/class_s_index/', teacher.classroom_s_index, name='teacher_class_s_index'),
    path('Teachers/s_details/', teacher.s_details, name='teacher_s_details'),
    path('Teachers/ass_assign/', teacher.ass_assign, name='teacher_ass_assign'),

    path('Parents/home/', parent.login, name='parent_login'),
    path('Parents/s_index/', parent.s_index, name='parent_s_index'),
    path('Parents/c_index/', parent.c_index, name='parent_c_index'),
    path('Parents/s_detail/', parent.s_details, name='parent_s_detail'),

]


