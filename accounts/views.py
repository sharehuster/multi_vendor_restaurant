from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User

# Create your views here.

def registerUser(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)

        if form.is_valid():

            '''
            # create the user using the form
            password = form.cleaned_data['password']
            user = form.save(commit=False) # đang lưu dữ liệu từ form vào một đối tượng, nhưng chưa thực hiện ghi vào cơ sở dữ liệu
            user.role = User.CUSTOMER
            user.set_password(password)
            user.save()
            form.save()
            return redirect('registerUser')
            '''

            # create the user using create_user method (models.py)

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            # objects là một quản lý (manager) mặc định của model User, cung cấp các phương thức truy vấn để làm việc với cơ sở dữ liệu
            user.role = User.CUSTOMER
            user.save()
        else:
            print('invalid form')
            print(form.errors)

    else:
        form = UserForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/registerUser.html', context)