from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from test_app.models import contact
from test_app.forms import NameForm



def index_view(request):
    return render(request, 'test_app/index.html')

def about_view(request):
    return render(request, 'test_app/about.html')

def contact_view(request):
    return render(request, 'test_app/contact.html')


def test2_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            print(name, subject, email, message)
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
            
        
        
    form = NameForm()   
    return render(request, 'test_app/test2.html',{'form':form})
