from django.shortcuts import render, get_object_or_404

# Create your views here.
def about(request):
    return render(request, 'sitepages/about.html')
