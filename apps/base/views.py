from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# Create your views here.


def index(request):
	return render(request, 'feria/index.html')
