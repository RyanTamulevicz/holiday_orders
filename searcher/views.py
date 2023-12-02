from django.shortcuts import render


# Create your views here.
# make a search view
def search(request):
    return render(request, "index.html")
