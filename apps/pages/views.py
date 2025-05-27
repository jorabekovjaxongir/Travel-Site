from django.shortcuts import render
from apps.pages.models import TourCategory
from apps.package.forms import SubscriptionForm


def destination(request):
    return render(request, 'destinational.html')

def explore_tour(request):
    return render(request, 'tour.html', context={
        'tour_category' : TourCategory.objects.all(),
        "subs": SubscriptionForm(request.POST or None)
    })

def travel_booking(request):
    return render(request, 'booking.html')

def our_gallery(request):
    return render(request, 'gallery.html')

def travel_guides(request):
    return render(request, 'guides.html')

def testimonial(request):
    return render(request, 'testimonial.html')