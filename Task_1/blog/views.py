from django.shortcuts import render
from django.http import HttpResponse

L=[]
for i in range(1,21):
    L.append(i)
# Create your views here.
def home(request):
    context={
        'lists':L,
    }
    return render(request,'Blog/home.html',context)

def about(request):
    return render(request,'Blog/about.html',{'title':'About'})

def nos(request):
    first_no = int(request.GET['fname'])
    last_no = int(request.GET['lname'])
    M=[]

    if first_no<last_no:
        for i in range(first_no,last_no):
            M.append(i)
        context={
            'lists':M,
        }
        return render(request,'nos.html',context)
    else:
        return HttpResponse('<p>Starting number should be greater than Last number<p>')

