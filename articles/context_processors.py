from .models import Category


def categories(category):
    category = Category.objects.all().filter(active=True)
    return {
        'category': category,
    }
