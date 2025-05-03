from django.urls import path
from .views import (
    destinationView,
    explore_tourView,
    travel_bookingView,
    our_galleryView,
    travel_guidesView,
    testimonialView,
)


urlpatterns = [
    path('destination/',destinationView, name='destination'),
    path('explore_tour/',explore_tourView, name='explore_tour'),
    path('travel_booking/',travel_bookingView, name='travel_booking'),
    path('our_gallery/',our_galleryView, name='our_gallery'),
    path('travel_guides/',travel_guidesView, name='travel_guides'),
    path('testimonial/',testimonialView, name='testimonial'),
]
