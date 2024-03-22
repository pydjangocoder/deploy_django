from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    articles = Article.objects.all()

    context = {
        "title": "Главная страница",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


def category_page_view(request, category_id):
    articles = Article.objects.filter(
        category=category_id
    ).order_by(
        '-created_at'
    )
    trends = Article.objects.all().order_by('-views')

    context = {
        "title": f"Категория: {Category.objects.get(id=category_id)}",
        'articles': articles,
        'trends': trends
    }

    return render(request, "blog/category_page.html", context)


def about_us_page_view(request):
    return render(request, "blog/about_us.html")


def our_team_page_view(request):
    return render(request, "blog/our_team.html")


def services_page_view(request):
    return render(request, "blog/services.html")


def article_detail_page_view(request, article_id):
    article = Article.objects.get(id=article_id)
    last_articles = Article.objects.all().order_by('-created_at')[:3]
    if article.author != request.user:
        article.views += 1
        article.save()

    context = {
        "title": f"Статья: {article.title}",
        "article": article,
        "last_articles": last_articles
    }
    if request.user.is_authenticated:
        context.update({
            "form": CommentForm()
        })

    return render(request, "blog/article_detail.html", context)


@login_required(login_url="login")
def add_article_view(request):
    if request.method == 'POST':
        form = AddArticleForm(data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Статья успешно добавлена !")
            return redirect('article_detail', article.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('add_article')
    elif request.method == 'GET':
        form = AddArticleForm()

    context = {
        'title': 'Добавить статью',
        'form': form
    }

    return render(request, "blog/add_article.html", context)


def register_user_view(request):
    if request.method == 'POST':
        form = RegistrationUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            profile_user = Profile.objects.create(user=user)
            profile_user.save()
            messages.success(request, "Вы успешно прошли регистрацию !")
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect('register')
    else:
        form = RegistrationUserForm()

    context = {
        'title': "Регистрация пользователя",
        'form': form
    }

    return render(request, "blog/register.html", context)


def login_user_view(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                messages.info(request, "Вы вошли в аккаунт !")
                return redirect('index')
            else:
                messages.error(request, "Логин или пароль неверный !")
                return redirect('index')
        else:
            messages.error(request, "Логин или пароль неверный !")
            return redirect('index')


    else:
        form = LoginUserForm()

    context = {
        'title': "Вход пользователя",
        'form': form
    }

    return render(request, "blog/login.html", context)


@login_required(login_url="login")
def logout_user_view(request):
    logout(request)
    messages.info(request, "Вы вышли с аккаунта !")
    return redirect('index')


def search_view(request):
    word = request.GET.get('q')
    categories = Category.objects.all()
    articles = Article.objects.filter(
        title__iregex=word
    )

    context = {
        "title": "Результаты поиска",
        "categories": categories,
        "articles": articles
    }

    return render(request, "blog/index.html", context)


@login_required(login_url="login")
def update_article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        form = AddArticleForm(instance=article,
                              data=request.POST,
                              files=request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.success(request, "Детали успешно обновлены !")
            return redirect("article_detail", article.id)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
            return redirect("update_article", article.id)
    else:
        form = AddArticleForm(instance=article)
    context = {
        "form": form,
        "title": "Изменить статью"
    }
    return render(request, "blog/add_article.html", context)


@login_required(login_url="login")
def delete_article_view(request, article_id):
    article = Article.objects.get(id=article_id)
    if request.method == "POST":
        article.delete()
        messages.warning(request, "Статья удалена !")
        return redirect("index")
    context = {
        "article": article,
        "title": "Удалить статью"
    }

    return render(request, "blog/delete_article.html", context)


def check_profile(request, user_id):
    user = User.objects.get(id=user_id)
    profile_user = Profile.objects.get(user=user)
    articles = Article.objects.filter(author=user_id).order_by('-views')[:4]

    context = {
        "title": "Профиль",
        "user": user,
        "profile": profile_user,
        "articles": articles
    }

    return render(request, "blog/profile.html", context)


@login_required(login_url="login")
def update_profile_view(request, user_id):
    user = User.objects.get(id=user_id)
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        user_form = UserForm(instance=user,
                             data=request.POST)
        profile_form = ProfileForm(instance=profile,
                                   data=request.POST,
                                   files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Данные успешно обновлены !")
            return redirect("profile", user.id)
        else:
            for field in user_form.errors:
                messages.error(request, user_form.errors[field].as_text())
            for field in profile_form.errors:
                messages.error(request, profile_form.errors[field].as_text())

            return redirect("edit_profile", user.id)

    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
        "title": "Изменить профиль"
    }

    return render(request, "blog/edit_profile.html", context)
