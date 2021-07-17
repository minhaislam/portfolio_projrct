from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def portfolio(request):
    # return HttpResponse('my Portfloio')
    return render(request,'portfolio_page.html')