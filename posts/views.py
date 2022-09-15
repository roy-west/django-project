from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import Http404
import random


def post_search_view(request):
    query_dict = request.GET
    query_data = query_dict.get("query")
    object_from_db = None
    try:
        if query_data:
            if int(query_data):
                object_from_db = Post.objects.get(id=query_data)
        else:
            object_from_db = None
    except Post.DoesNotExist:
        raise Http404
    except:
        object_from_db = "Вам нужно передавать только числа !"

    context = {
        "object": object_from_db
    }
    return render(request, 'posts/post_search.html', context=context)


def post_list_view(request):
    print(request.method)
    my_object = Post.objects.all()
    len_of_objects = len(my_object)
    my_random_object_from_db = Post.objects.get(id=random.randint(1, len_of_objects))
    all_posts = Post.objects.all()
    context = {"my_first_object": my_random_object_from_db,
               "posts": all_posts}

    return render(request, 'posts/test.html', context=context)


def post_detail_view(request, id=None):
    post_object = None
    print(type(id))
    print(id)
    if id is not None:
        try:
            post_object = Post.objects.get(id=id)
        except:
            post_object = " Hey ! It's post_detail_view"

    context = {
        "post_object": post_object
    }
    return render(request, 'posts/post_detail.html', context=context)


def post_create_view(request):
    print(request.GET)
    print(request.POST)
    context = {}
    return render(request, 'posts/post_create.html', context=context)

