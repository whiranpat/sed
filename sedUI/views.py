from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'sedUI/pages/index.html')

def contact(request):
    return render(request, 'sedUI/pages/contact.html')

def login(request):
    return render(request, 'sedUI/pages/basic.html')

def registration(request):
    return render(request, 'sedUI/pages/registration.html')

def loginOrRegister(request):
    return render(request, 'sedUI/pages/loginOrRegister.html')

def courses(request):
    return render(request, 'sedUI/pages/courses.html')

def scouts(request):
    return render(request, 'sedUI/pages/scouts.html')

def profile(request):
    return render(request, 'sedUI/pages/profile.html')

def about(request):
    return render(request, 'sedUI/pages/about.html')

