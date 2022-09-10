from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import Http404
import random


def post_search_view(request):
    # TODO: Переопределить view так, чтобы он выводил нужную запись,
    #  если query_data может преобразовываться в int
    #  иначе выдаете object_from_db пустым
    query_dict = request.GET
    query_data = query_dict.get("query")
    object_from_db = None
    if query_data is not None:
        object_from_db = Post.objects.get(id=query_data)

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
            raise Http404

    context = {
        "post_object": post_object
    }
    return render(request, 'posts/post_detail.html', context=context)
