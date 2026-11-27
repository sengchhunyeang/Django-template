from django.http import Http404
from django.shortcuts import render

# ទិន្នន័យគំរូ (មិនទាន់ប្រើ database)
STUDENTS = [
    {"id": 1, "name": "Sok Dara", "class_name": "Class A", "score": 92.5},
    {"id": 2, "name": "Chan Sreyneang", "class_name": "Class A", "score": 85},
    {"id": 3, "name": "Kim Vuthy", "class_name": "Class B", "score": 78.25},
]


def student_list(request):
    context = {"title": "Student List", "students": STUDENTS}
    return render(request, "students/student_list.html", context)


def student_detail(request, student_id):
    for student in STUDENTS:
        if student["id"] == student_id:
            return render(request, "students/student_detail.html", {"student": student})
    raise Http404("Student not found")
