from  django.shortcuts import render
from articals.models import Post


def home(request):
    posts=Post.objects.all()

    context={
        'posts':posts
    }

    return render(request,'home.html',context)
def showArticle(request,pk):
    singlepost=Post.objects.get(id=pk)

    context={
        'singlepost':singlepost
    }

    return render(request,'detailsArticle.html',context)    