from django.shortcuts import render
from .forms import StudentRegister
from .models import User

def create(request):
    if request.method == 'POST':
        fm = StudentRegister(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegister()

    # Retrieve all users from the User model
    users = User.objects.all()

    return render(request, 'enroll/create.html', {'form': fm, 'users': users})
