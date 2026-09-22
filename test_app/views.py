from django.shortcuts import render

def index_view(request):
    return render(request, 'test_app/index.html')

def about_view(request):
    return render(request, 'test_app/about.html')

def contact_view(request):
    return render(request, 'test_app/contact.html')

def test_view(request):
    return render(request, 'test_app/test.html',{'name':'Mobina','lastname':'KH'})
