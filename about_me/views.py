from django.shortcuts import render

def about_me(request):
    return render(request, '../templates/about-me/about-me.html')