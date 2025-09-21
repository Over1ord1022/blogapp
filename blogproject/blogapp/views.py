from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost, Category
from .forms import PreferencesForm
from django.utils import timezone

# Пример данных 
SAMPLE_POSTS = [
    {
        'id': 1,
        'title': 'Введение в Django',
        'content': 'Django - это мощный фреймворк для веб-разработки на Python...',
        'author': 'Иван Иванов',
        'category': 'Программирование',
        'created_at': timezone.now(),
        'image': 'images/django-logo.png'
    },
    {
        'id': 2,
        'title': 'Искусство кулинарии',
        'content': 'Кулинария - это не просто приготовление пищи, это искусство...',
        'author': 'Мария Петрова',
        'category': 'Кулинария',
        'created_at': timezone.now(),
        'image': 'images/cooking.jpg'
    }
]

SAMPLE_CATEGORIES = [
    {'id': 1, 'name': 'Программирование'},
    {'id': 2, 'name': 'Кулинария'},
    {'id': 3, 'name': 'Путешествия'},
    {'id': 4, 'name': 'Спорт'},
]

def get_user_preferences(request):
    """Получаем настройки пользователя из cookies"""
    theme = request.COOKIES.get('theme', 'light')
    language = request.COOKIES.get('language', 'ru')
    return {'theme': theme, 'language': language}

def home(request):
    preferences = get_user_preferences(request)
    
    context = {
        'posts': SAMPLE_POSTS,
        'categories': SAMPLE_CATEGORIES,
        'preferences': preferences
    }
    
    response = render(request, 'blogapp/home.html', context)
    return response

def preferences(request):
    if request.method == 'POST':
        form = PreferencesForm(request.POST)
        if form.is_valid():
            # Сохраняем настройки в cookies
            response = redirect('home')
            response.set_cookie('theme', form.cleaned_data['theme'], max_age=365*24*60*60)
            response.set_cookie('language', form.cleaned_data['language'], max_age=365*24*60*60)
            return response
    else:
        preferences = get_user_preferences(request)
        form = PreferencesForm(initial=preferences)
    
    return render(request, 'blogapp/preferences.html', {'form': form})

def post_detail(request, post_id):
    post = next((p for p in SAMPLE_POSTS if p['id'] == post_id), None)
    if not post:
        return HttpResponse("Пост не найден")
    
    preferences = get_user_preferences(request)
    
    return render(request, 'blogapp/post_detail.html', {
        'post': post,
        'preferences': preferences
    })