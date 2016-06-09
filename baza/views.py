from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'baza\post_list.html', {'posts': posts})

    # render pobiera dane z apki sieciowej (nowe elementy)
    # 'posts': posts określa z czego korzysta template
