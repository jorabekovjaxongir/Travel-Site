from django.urls import path
from .views import (
    destination,
    explore_tour,
    travel_booking,
    our_gallery,
    travel_guides,
    testimonial,
)


urlpatterns = [
    path('destination/',destination, name='destination'),
    path('explore_tour/',explore_tour, name='explore_tour'),
    path('travel_booking/',travel_booking, name='travel_booking'),
    path('our_gallery/',our_gallery, name='our_gallery'),
    path('travel_guides/',travel_guides, name='travel_guides'),
    path('testimonial/',testimonial, name='testimonial'),
]
