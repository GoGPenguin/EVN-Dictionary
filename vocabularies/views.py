from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Translation, Vocabulary

# Create your views here.
def get_vocabularies(request):
    data = Translation.objects.all()
    a = Vocabulary.objects.all()
    context = {'data': data, 'a': a}
    return render(request, 'home.html', context)

def get_index_page (request):
    return render(request,'index_template.html')

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('searchInput', '')
        # Tìm kiếm từ vựng hoặc phần loại từ có chứa từ khóa search_query
        results = Translation.objects.filter(vocab__vocab_en__exact=search_query) | \
          Translation.objects.filter(pos__pos_type__exact=search_query)
        print(results)
        # return render(request, 'search_template.html', {'results': results, 'search_query': search_query})
    return render(request, 'search_template.html',{'results':results,'search_query':search_query})
        