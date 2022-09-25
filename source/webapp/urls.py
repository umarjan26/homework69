from django.urls import path

from source.webapp.views import index_view

app_name = 'webapp'

urlpatterns = [
    path('', index_view)
]
