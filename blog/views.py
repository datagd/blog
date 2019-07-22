from django.shortcuts import render, get_object_or_404
from .models import BlogArticles

# Create your views here.


def blog_title(request):  #参数request负责响应所接受的请求，必不可少的参数
    blogs = BlogArticles.objects.all() #得到所有的BlogArticle的对象实例
    return render(request, "blog/title.html", {"blogs":blogs})

def blog_article(request, article_id):
    #article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)
    #get_object_or_404这个方法能够简化我们对请求网页不存在的异常处理
    pub = article.publish
    return render(request, "blog/content.html", {"article":article, "publish":pub})