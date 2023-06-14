from django.shortcuts import render

# Create your views here.
def testimonialPageView(request):
    render(request, 'testimonials.html')