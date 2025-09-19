from django.shortcuts import render

def communication(request):
    return render(request, '../templates/communication/communication.html')