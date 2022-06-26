from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'articles_index.html', {'articles': articles})


def detail(request):
    article = Article.objects.get(pk=1)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            
            return redirect('detail')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles_detail.html', {'article': article, 'form': form})