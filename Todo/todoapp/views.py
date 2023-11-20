from django.shortcuts import render,HttpResponse
from django.views import View
from . models import *
# Create your views here.

class CreateTask(View):

    def get(self,request):
        return render(request,'create_task.html')
    
    def post(self,request):
        #data fetch from form 
        t = request.POST['title']
        det = request.POST['det']
        cat = request.POST['cat']
        date = request.POST['due_date']


        # data validation
        task = Todo.objects.create(title=t,detail=det,cat=cat,due_date=date)
        return HttpResponse("Data fetched")

    



# def home(request):
#     return render(request,'create_task.html')