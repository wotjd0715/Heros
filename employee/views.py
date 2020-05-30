from django.shortcuts import render, redirect
from employee.models import Article
# Create your views here.
def employee_all(request):
    articles = Article.objects.all()
    return render(request, 'employee/employee_list.html', { 'articles':articles })

def new_feed(request):
    if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['author'] != '' and request.POST['title'] != '' and request.POST['price'] != '' and request.POST['text'] != '' and \
                request.POST['place'] != '':
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                place=request.POST['place'],
                price=request.POST['price'],
                text=request.POST['text']
            )

            # 새글 등록 끝
        return redirect(f'/employee/feed/{new_article.pk}')
    return render(request, 'employee/new_feed.html')

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'employee/detail_feed.html', {'feed': article})


def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.delete()
            return redirect('/employee/')  # 첫페이지로 이동하기

    return render(request, 'employee/remove_feed.html', {'feed': article})

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.place = request.POST['place']
            article.price = request.POST['price']
            article.text = request.POST['text']
            article.save()
            return redirect(f'/employee/feed/{ article.pk }')

    return render(request, 'employee/edit_feed.html', {'feed': article})