from django.shortcuts import render

# Create your views here.
def home(request):
    """view that serve homepage"""
    return render(request, "index.html", {})