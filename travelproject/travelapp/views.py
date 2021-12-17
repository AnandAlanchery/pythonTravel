from django.shortcuts import render
from .models import Place,Team
# Create your views here.
def index(request):
    obj=Place.objects.all()
    obj2=Team.objects.all()
    return render(request,'index.html',{'result':obj,'change':obj2})