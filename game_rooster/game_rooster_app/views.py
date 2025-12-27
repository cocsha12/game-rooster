from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')



def auth(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        # \n (терминальный n) - это перенос строки
        print('Почта: '+ email, '\n', 'Пароль: '+ password, sep='')
    return render(request, 'auth.html')

def reg(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        birthday = request.POST.get('birthday')
        username = email

        print('Почта: ', email, '\n', 'Пароль: ', password, 'Имя: ', first_name, sep='')

        user = User.objects.create_user(username, email, password)

        return JsonResponse({'status': 'success', 'message': 'Everything OK'})


    return render(request, 'reg.html')

    

