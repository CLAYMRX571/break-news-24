from .models import Category, Tag

def get_main_context(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        "tags": tags,
        "categories": categories,
    }
    return context