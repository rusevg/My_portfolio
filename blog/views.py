from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, CommentPost
from django.core.paginator import Paginator
from .forms import CommentForm

def all_blogs(request):
    blog_count = Blog.objects
    blogs = Blog.objects.order_by('-date')
    paginator = Paginator(blogs, 4)
    page_number = request.GET.get("page", 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
        'blogs': page,
        'blog_count': blog_count,
        'next_url': next_url,
        'prev_url': prev_url,
        'is_paginated': is_paginated,
    }
    return render(request, 'blog/all_blogs.html', context=context)

def detail(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    all_comments = blog.comments.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.blog_c = blog
            # Save the comment to the database
            new_comment.save()
            return redirect(request.path)
    else:
        comment_form = CommentForm()
    return render(request,'blog/detail.html', {"blog":blog, "comment_form":comment_form, "all_comments":all_comments})

'''
hui pizda djigurda
'''
