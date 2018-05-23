from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from .forms import UploadFileForm


def index(request):
    response = "placeholder to later display all the list of blogs"
    request.session['blogName'] = "Esther's Test Blog"
    print ("*"*150, request.session['blogName'])
    return render(request, "blogs/index.html")

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    request.session['blogName'] = request.POST['blog-name']
    return redirect('/')

def show(request, blogNum):
    response = "placeholder to display blog " + str(blogNum)
    return HttpResponse(response)

def edit(request, blogNum):
    response = "placeholder for editing blog " + str(blogNum)
    return HttpResponse(response)

def destroy(request,blogNum):
    return redirect('/')


def upload_file(request):
    if request.method == "POST":
        print("*"*150, "got to upload_file")
        form = UploadFileForm(request.POST, request.FILES)
        print("*"*150, form.errors)
        if form.is_valid():
            print("*"*150, "got to is_valid")
            # need to actually make this function:
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/upload')
    else:
        form = UploadFileForm()
    return render(request, 'blogs/upload.html', {'form': form})

def handle_uploaded_file(f):
    print("*"*150, "got to handle_upload_file")
    with open('/Users/estherting/desktop/file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def success_upload(request):
    return redirect('/')
    return HttpResponse("Successful upload!")
