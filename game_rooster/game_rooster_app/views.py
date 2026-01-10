from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import, logout login
from django.http import JsonResponse


def index(request):
    try:
        context = { 'username' : request.user.username }
        return render(request, 'index.html', context)
    except AttributeError as e:
        return render(request, 'index.html')
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'status': 'success'})



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

        login(request, user)

        return JsonResponse({'status': 'success'})


    return render(request, 'reg.html')

    

