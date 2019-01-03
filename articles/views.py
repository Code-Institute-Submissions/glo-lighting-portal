from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all().order_by("date")
    return render(request, "articles/article_list.html", {"articles": articles})


# def post_detail(request, slug=slug):
#     template = 'articles/post_detail.html'
    
#     post = get_object_or_404(Post, slug=slug)
#     context = {
#     'post':post,
#     }
#     return render(request, template, context)

# def category_detail(request, slug):
#     template = 'articles/article_list.html'
    
#     category = get_object_or_404(Category, slug=slug)
#     post = Post.objects.filter(category=category)