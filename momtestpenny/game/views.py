from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request, 'game.html', {'foo':'bar'},
    content_type='application/xhtml+xml')

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")