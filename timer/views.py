from django.shortcuts import render

def timer_page(request):
    return render(request, 'timer/timer_page.html')
