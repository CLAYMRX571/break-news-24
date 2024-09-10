from .models import Category, Tag, Article
from datetime import datetime

def get_main_context(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    latest_news = Article.objects.filter()[:4]
    today_date = datetime.now().date()

    context = {
        "tags": tags,
        "today_date": today_date,
        "categories": categories,
        "latest_news": latest_news,
    }
    return context 