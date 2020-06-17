from django.shortcuts import render, redirect
from managing.models import *
from django.core.paginator import Paginator
# 공지사항 전체 보기 기능
def Notice_all(request):
    notice = Notice.objects.all()
    paginator = Paginator(notice, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    page_title = "Notice"
    return render(request, 'managing/Notice.html', {'notice': notice, 'posts': posts, 'page_title':page_title})
#FAQ전체글 보기 기능
def FAQ_all(request):
    faq = FAQ.objects.all()
    paginator = Paginator(faq, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    page_title = "FAQs"
    return render(request, 'managing/Notice.html', {'faq': faq, 'posts': posts, 'page_title':page_title})
#공지사항 세부 내용보기 기능
def Notice_detail(request, pk):
    notice = Notice.objects.get(pk=pk)
    feed_text=notice.text
    feed_text_list=feed_text.split('\n')
    return render(request, 'managing/Notice_detail.html', {'feed':notice, 'feed_text_list':feed_text_list})
#FAQ 세부 내용보기 기능 
def FAQ_detail(request, pk):
    faq = FAQ.objects.get(pk=pk)
    feed_text=faq.text
    feed_text_list=feed_text.split('\n')
    return render(request, 'managing/FAQ_detail.html', {'feed':faq, 'feed_text_list':feed_text_list})