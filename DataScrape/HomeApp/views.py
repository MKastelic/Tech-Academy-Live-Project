from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Home/index.html') # I think render methods automatically use the RequestContext class? Ask Sean about this