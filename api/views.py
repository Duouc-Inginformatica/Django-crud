from email import message
from re import I
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import Maule

# Create your views here.

class MauleViews(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return render(request, 'index.html')
    
    def put(self, request):
        return render(request, 'index.html')

    def delete(self, request):
        return render(request, 'index.html')