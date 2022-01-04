from django.http import HttpResponse

COUNTER = 0


def index(request):
    return HttpResponse("<h2>Главная</h2>")


def about(request, counter_value=0):
    global COUNTER
    COUNTER = counter_value
    output = f"<h2>Значение счетчика: {COUNTER}</h2>"
    return HttpResponse(output)


def contact(request, user_name='Tom'):
    output = f"<h2>Имя пользователя: {user_name}<h2>"
    return HttpResponse(output)
