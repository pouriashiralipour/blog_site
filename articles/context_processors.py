from .models import Category, Tags


def categories(category):
    category = Category.objects.all().filter(active=True)
    return {
        'category': category,
    }


def tags(tag):
    tag = Tags.objects.all().filter(active=True)
    return {
        'tag': tag,
    }