from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField('student status', default=False)
    is_teacher = models.BooleanField('teacher status', default=False)
    is_parent = models.BooleanField('parent status', default=False)


class Courses(models.Model):
    title = models.CharField(max_length=50)
    CATEGORIES = (
        ('ENG', 'English'),
        ('MATH', 'Mathematics'),
        ('LANG', 'Foreign Language'),
        ('HIST', 'History'),
        ('SCI', 'Science')
    )
    category = models.CharField(
        choices=CATEGORIES,
        default=None,
        max_length=50,
    )
    course_number = models.IntegerField()


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10, default='0000000000')
    courses = models.ManyToManyField(Courses)
    

class Assignment(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='assignments')
    due_date = models.DateField()
    description = models.TextField(max_length=300)
    title = models.CharField(max_length=50)
    document = models.FileField()


class Parent(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    phone_number = models.CharField(max_length=10, default='0000000000')

class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    courses = models.ManyToManyField(Courses)
    assignments = models.ManyToManyField(Assignment)
    teacher = models.ManyToManyField(Teacher)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

class Classroom(models.Model):
    courses = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    room_number = models.IntegerField()
    students = models.ManyToManyField(Student)
    assignment = models.ManyToManyField(Assignment)
    time = models.TimeField()