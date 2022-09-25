import json
from datetime import datetime
from http import HTTPStatus

from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == "GET":
        return HttpResponse()
    return HttpResponseNotAllowed(["GET"])


def echo_view(request):
    response_data = {
        "method": request.method,
        "datetime": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if request.body:
        response_data["body"] = json.loads(request.body)

    response = JsonResponse(response_data)

    return response


def add_view(request):
    if request.method == "POST":
        operation = 'add'
        print(operations(request.body, operation))

        return operations(request.body, operation)

    return HttpResponseNotAllowed(["POST"])


def subtract_view(request):
    if request.method == "POST":
        operation = 'subtract'
        return operations(request.body, operation)

    return HttpResponseNotAllowed(["POST"])


def multiply_view(request):
    if request.method == "POST":
        operation = 'multiply'
        return operations(request.body, operation)

    return HttpResponseNotAllowed(["POST"])


def divide_view(request):
    if request.method == "POST":
        operation = 'divide'
        return operations(request.body, operation)

    return HttpResponseNotAllowed(["POST"])


def operations(request_body, operation):
    response_data = {}
    print("test")
    status = True

    number1, number2 = json.loads(request_body).values()
    try:
        number1, number2 = int(number1), int(number2)
        if operation == 'subtract':
            result = number1 - number2
            response_data["answer"] = result
        elif operation == 'add':
            result = number1 + number2
            response_data["answer"] = result
        elif operation == 'multiply':
            result = number1 * number2
            response_data["answer"] = result
        elif operation == 'divide':
            result = number1 / number2
            response_data["answer"] = result
    except TypeError as e:
        response_data["error"] = str(e)
        status = False
    except ZeroDivisionError as e:
        response_data["error"] = str(e)
        status = False
    except ValueError as e:
        response_data["error"] = 'Empty fields'
        status = False

    if status:
        response = JsonResponse(response_data, status=HTTPStatus.OK)
        print(response_data)
    else:
        response = JsonResponse(response_data, status=HTTPStatus.BAD_REQUEST)

    return response
