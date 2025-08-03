from django.shortcuts import render, redirect, get_object_or_404
from .models import assignment4app
from .forms import StudentForm

def student_list(request):
    students = assignment4app.objects.all() 
    return render(request, 'assignment4app/student_list.html', {'students': students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'assignment4app/create_student.html', {'form': form})

def update_student(request, pk):
    student = get_object_or_404(assignment4app, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'assignment4app/create_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(assignment4app, pk=pk)
    student.delete()
    return redirect('student_list')

