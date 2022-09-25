from django.shortcuts import render
from source.api_v1.views import get_csrf_token_view



def index_view(request):
    return render(request, 'index.html')
