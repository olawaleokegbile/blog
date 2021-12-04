from django.shortcuts import render, redirect
from . models import Contact, Post
from django.core.paginator import Paginator
from .forms import CommmentForm, ContactForm
from django.core.mail import mail_admins, send_mail, BadHeaderError
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    posts = Post.objects.all() 
    p = Paginator(posts, 4) 
    page = request.GET.get('page')
    page_num = p.get_page(page)
    return render(request, 'blog.html', {'posts': posts, 'page_num': page_num})

def post(request, pk):
    posts = Post.objects.get(id=pk)

    if request.method == 'POST':
        form = CommmentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = posts
            obj.save()

            return redirect('post', pk=posts.pk)
    else:
        form = CommmentForm()
    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'post.html', context)

def contact(request):
    if request.method == 'POST':
        forms = ContactForm(request.POST)

        if forms.is_valid():
            subject = f"Message from {forms.cleaned_data['name']}"
            message = forms.cleaned_data['message']
            sender = forms.cleaned_data['email']
            mail_admins(sender, message, subject)

            forms.save()
            messages.add_message(request, messages.INFO, 'Contact Submitted.')
            return redirect('contact')

    else:
        forms = ContactForm()
    context = {
        'forms': forms
    }
    return render(request, 'contact.html', context)
