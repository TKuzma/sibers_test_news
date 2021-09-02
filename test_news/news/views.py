from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import Article
from .forms import ArticleForm

class NewsListView(ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 10
    
    def get(self, request):
        paginate_by = request.GET.get('paginate_by', 10) or 10
        data = self.model.objects.all()

        paginator = Paginator(data, paginate_by)
        page = request.GET.get('page')

        try:
            paginated = paginator.get_page(page)
        except PageNotAnInteger:
            paginated = paginator.get_page(1)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)

        return render(request, self.template_name, {'DataPaginated':paginated, 'paginate_by':paginate_by})
    

def add_article(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Incorrect form'

    form = ArticleForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'add_article.html', data)



