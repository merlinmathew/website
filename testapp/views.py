from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,"testapp/index.html")


def about(request):
    return render(request,"testapp/about.html")

def contact(request):
    return render(request,"testapp/contact.html")


def blog(request):
    return render(request,"testapp/blog-rightsidebar.html")