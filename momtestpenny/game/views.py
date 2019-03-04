from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request, 'game.html', "Hello World" , content_type='application/xhtml+xml')
