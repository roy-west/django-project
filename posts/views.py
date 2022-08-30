from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
import random


# Create your views here.

def main_page(request):
    return HttpResponse("Hello, World !")


def test_view(request):
    print(request)
    my_object = Post.objects.all()
    len_of_objects = len(my_object)
    my_random_object_from_db = Post.objects.get(id=random.randint(1, len_of_objects))
    list_ids = [1, 4, 2]
    all_items_from_db = Post.objects.filter(id__in=list_ids)
    context = {"my_first_object": my_random_object_from_db,
               "my_list": all_items_from_db}

    return render(request, 'posts/test.html', context=context)
