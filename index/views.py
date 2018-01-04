
from django.shortcuts import render
from .models import Articles
# Create your views here.
def index(request):
    return render(request, 'index/wrapper.html', {'object_list': Articles.objects.all()})