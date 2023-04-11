from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import Post
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import PostForm
# from django.contrib.auth import login_required

@login_required
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog-main-page.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# def login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('post_list')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/register.html', {'form': form})

def blog(request, post_id):
    post = Post.objects.get(id=post_id)
    # if the methode is Post
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
    # If the form is valid
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    #yes, save

    # #redirect to home
    # No, Show Error
        else:
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, "blog-view.html", {'post': post})

