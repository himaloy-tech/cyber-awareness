from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from .models import Contact, Article, Comment, Video
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "Articles" : Article.objects.all().order_by('id')[:3],
        "Videos" : Video.objects.all().order_by('id')[:3],
    })


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        obj = Contact.objects.create(name=name, message=message, email=email)
        obj.save()
        messages.success(request, "<strong>Success!</strong> Your Query has been Successfully Submitted")
        return HttpResponseRedirect(reverse("index"))
    else:
        return redirect('/')

def articleView(request, articleId):
    article = Article.objects.get(id=articleId)
    return render(request, "articleView.html", {
        "article": article,
        "articleId" : articleId
    })

def PostComment(request):
    if request.method == "POST":
        text = request.POST.get('text')
        id = request.POST.get('articleId')
        comment = Comment(article=Article.objects.get(id=id), comment=text)
        comment.save()
        return JsonResponse({
            "message" : "Comment Posted Successfully"
        })

def comment(request, articleId):
    comments = Comment.objects.filter(article__id=articleId).order_by('-time')
    return JsonResponse([comment.serialize() for comment in comments], safe=False)


def articlehub(request):
    return render(request, "articlehub.html", {
        "Articles" : Article.objects.all().order_by('id')
    })