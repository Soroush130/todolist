from django.shortcuts import render


def header(request):
    return render(request, 'shared/Header.html', {})


def footer(request):
    return render(request, 'shared/Footer.html', {})


def page_404(request):
    return render(request, '404.html')
