from django.shortcuts import render
from .models import About,Category,Guide


def aboutView(request):
    return render(request, 'about.html', context={
        'abouts': About.objects.first(),
        'categories': Category.objects.all(),
        'guides': Guide.objects.all(),
    })