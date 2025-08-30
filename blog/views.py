from django.shortcuts import render, get_list_or_404
from blog.models import Post
from django.http import Http404
# Create your views here.

# Ccreating a view to display the list of posts.
def post_list(request):
    posts = Post.published.all()
    dict = {'posts': posts}
    return render(request, 'blog/post/list.html', context=dict)

#  Create a second view to display a single post.
def post_detail(request, year, month, day, post):
    post = get_list_or_404(Post,
                           status= Post.Status.PUBLISHED,
                           slug=post,
                           publish__year=year,
                           publish__month=month,
                           publish__day=day
                           )
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404('No Post found.')
    
    dict = {'post': post}
    return render(request, 'blog/post/detail.html', context=dict)