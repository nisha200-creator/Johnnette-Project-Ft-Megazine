from django.shortcuts import render
from .models import Category, Megazine, Crd, FeaturedPost,  LeftContent

def Myindex(request):
    Categorys = Category.objects.all()
    featured_post = Megazine.objects.filter(is_featured=True)
    crd_list = Crd.objects.all()
    featured_posts = FeaturedPost.objects.all()
    LeftContent_post = LeftContent.objects.all()
    

    content = {
        'Categorys': Categorys,
        'featured_post': featured_post,
        'Crd': crd_list,  
        'featured_posts': featured_posts,
        'LeftContent_post': LeftContent_post
    }

    return render(request, 'index.html', content)


