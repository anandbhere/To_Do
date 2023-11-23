from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from . models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class CreateTask(View):

    def get(self,request):
        
        if request.user.is_authenticated:
            return render(request,'create_task.html')
        else:
            context = {"msg":"You must login first to create tasks"}
            return redirect('/',context)
    
    def post(self,request):
        #data fetch from form 
        t = request.POST['title']
        det = request.POST['det']
        cat = request.POST['cat']
        date = request.POST['due_date']
        u = request.user

        # data validation
        task = Todo.objects.create(title=t,detail=det,cat=cat,due_date=date,uid = u)
        return HttpResponse("Data fetched")

    


class ViewTask(View):
    def get(self,request):
        tasks = Todo.objects.all()
        print(tasks)
        context = {'tasks':tasks}
        print(tasks)
        return render(request,'ViewTask.html',context)
        
    
class UpdateTask(View):
    def get(self,request,id):
        t = Todo.objects.get(id=id,uid = request.user)[0]
        print(t.due_date)
        print(type(t.due_date))
        context = {'tasks':t}
        return render(request,'UpdateTask.html', context)

    def post(self,request,id):
        t = request.POST['title']
        det = request.POST['detail']
        cat = request.POST['cat']
        dt = request.POST["due_date"]
        task = Todo.objects.update(title=t,detail=det,cat=cat,due_date=dt)

        return render(request,'create_task.html')

class DeleteTask(View):
    def get(self,request,pk):
        DeleteTask = Todo.objects.get(id=pk)
        print(DeleteTask)
        DeleteTask.delete()
        return render(request,'ViewTask.html')
    
class Register(View):
    def get(self,request):
        return render(request,'Register.html',)
    
    def post(self,request):
        uname = request.POST['uname']
        upass = request.POST['upass']
        ucpass = request.POST['ucpass']
        print(upass)
        print(ucpass)
        u = User.objects.create(username = uname)
        u.set_password(upass)
        u.save()
        return redirect('/')
       
    
class UserLogin(View):
    def get(self,request):
        return render(request,'Login.html')
    
    def post(self,request):
        uname = request.POST['uname']
        upass = request.POST['upass']
        context = {}


        u = authenticate(username = uname, password = upass)
        if u is not None:
            login(request,u)
            return redirect('/Dashboard')
        else:
            context['errmsg'] = "Invalid Username or Password"
            return render(request,"Login.html",context)
        #return HttpResponse('Loggedin successfullly')


class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('/')


class Dashboard(View):
    def get(self,request):
        if request.user.is_authenticated:
            t = Todo.objects.filter(uid=request.user)
            print(t)
            

            return render(request,'Dashboard.html',{'task' :t})
        else:
            redirect('/login')
