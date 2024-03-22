from django import template
from recipes.models import CarouselImage


register = template.Library()

@register.simple_tag()
def get_carousel_images():
    images = CarouselImage.objects.all()
    return images