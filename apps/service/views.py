from django.shortcuts import render
from . models import Service,FeedbackClient
from django  import template


register = template.Library()

@register.filter
def times(number):
    return range(number)

def serviceView(request):
    return render(request, 'services.html',context={
        'service1': Service.objects.all()[:1],
        'service2': Service.objects.all()[1:],
        'feedback_clients': FeedbackClient.objects.all(),
        })