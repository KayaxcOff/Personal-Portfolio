from django.shortcuts import render

def software_page(request):
    return render(request, '../templates/software/software.html')