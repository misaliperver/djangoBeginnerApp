from django.shortcuts import render # kendinden geldi



def index(request):
    return render(request, 'newpages/index.html')
