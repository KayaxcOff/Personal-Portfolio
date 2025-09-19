from django.shortcuts import render

def main_page(request):
    return render(request, '../templates/main-page/main-page.html')