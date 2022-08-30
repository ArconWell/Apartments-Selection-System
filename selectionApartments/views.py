from django.http import HttpResponse
from django.shortcuts import render

from selectionApartments.services.question_services import GetQuestionsInfoService

COUNTER = 0


def index(request):
    questions_info = GetQuestionsInfoService().execute()
    return render(request, "selectionApartments/index.html", {"questions": questions_info})


def about(request, counter_value=0):
    global COUNTER
    COUNTER = counter_value
    output = f"<h2>Значение счетчика: {COUNTER}</h2>"
    return HttpResponse(output)


def contact(request, user_name='Tom'):
    output = f"<h2>Имя пользователя: {user_name}<h2>"
    return HttpResponse(output)


def get_best_apartment(user_scores, user_priorities):
    user_result_scores = []
    apartments_expert_scores_list = []

    for i in range(len(user_scores)):
        user_result_score = user_scores[i] * user_priorities[i]
        user_result_scores.append(user_result_score)
    apartments_id = get_apartments_id()
    for id in apartments_id:
        apartments_expert_scores_list.append(get_apartment_expert_scores(id))

    delta = [0] * len(apartments_expert_scores_list[0])
    counter = 0
    while True:
        for i in range(len(apartments_expert_scores_list)):
            inner_flag = True
            for j in range(len(apartments_expert_scores_list[i])):
                if not apartments_expert_scores_list[i][j] - delta[j] < user_result_scores[j] < \
                       apartments_expert_scores_list[i][j] + delta[j]:
                    inner_flag = False
                    break
            if inner_flag:
                return apartments_id[i]
        counter += 1
        delta_index = nsmallest_index(delta, counter)
        delta[delta_index] += 0.05
        if counter == len(delta):
            counter = 0


def get_apartments_id():
    pass


def get_apartment_expert_scores(id):
    pass


def nsmallest_index(numbers: list, n: int) -> int:
    """
    Нахождение индекса n-го наименьшего элемента коллекции
    :param numbers: коллекция
    :param n: номер наименьшего элемента коллекции. Например, 1 - наименьший элемент коллекции, [длина коллекции] -
    наибольший элемент коллекции
    :return: индекс n-го наименьшего элемента коллекции
    """
    if not 0 < n <= len(numbers):
        raise IndexError("n должен быть меньше длины массива и больше нуля")
    numbers_min_indexes_list = []
    for i in range(n):
        numbers_min_value = numbers[0]
        numbers_min_index = 0
        for j in range(len(numbers)):
            if numbers[j] < numbers_min_value and j not in numbers_min_indexes_list:
                numbers_min_value = numbers[j]
                numbers_min_index = j
        numbers_min_indexes_list.append(numbers_min_index)
    return numbers_min_index
