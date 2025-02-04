from django.shortcuts import render


# Create your views here.
def index(request):
    Home = 'Дом'
    context = {
    'Home': Home,
    }
    return render(request, 'third_task/Home.html',context)

def index2(request):
    list1='Битва'
    context = {
    'list1':list1,
    }
    return render(request, 'third_task/list1.html',context)

def index3(request):
    list2 = 'Лавка'
    context = {
        'list2': list2,
    }
    return render(request, 'third_task/list2.html',context)


