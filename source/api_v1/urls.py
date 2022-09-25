from django.urls import path


from source.api_v1.views import echo_view, get_csrf_token_view, add_view, subtract_view, multiply_view, divide_view

app_name = 'api_v1'


urlpatterns = [
    path('echo/', echo_view),
    path("get-csrf-token/", get_csrf_token_view),
    path("add/", add_view),
    path("subtract/", subtract_view),
    path("add/", add_view, name='add'),
    path("multiply/", multiply_view),
    path('divide/', divide_view),
]
