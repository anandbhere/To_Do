from django.shortcuts import render,HttpResponse
from django.views import View

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

        print('Title', t)
        print('Details',det)
        print("Category", cat)
        print('date',date)


        # data validation
        return HttpResponse("Date fetched")

    



# def home(request):
#     return render(request,'create_task.html')