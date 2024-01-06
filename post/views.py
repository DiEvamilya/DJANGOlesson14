from django.shortcuts import render, redirect, get_object_or_404

from post.forms import PostCreateModelForm, PostUpdateModelForm
from post.models import Post, Tag


def post_list_view(request):

    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = Post.objects.get(pk=post_id)
        post.likes += 1
        post.save()
    context = {'posts': Post.objects.all(),
               'tag': Tag.objects.all()}
    return render(request, 'post_list.html', context)


def post_detail_view(request, slug):

    if request.method == 'POST':
        likes = request.POST.get('likes')
        likes = int(likes) + 1
    else:
        likes = 0

    context = {'post': Post.objects.get(slug=slug),
               'likes': likes,
               }

    return render(request, 'post_detail.html', context)



def post_create_view(request):

    form = PostCreateModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = PostCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
        else:
            context['form'] = form
    return render(request, 'create_post.html', context)


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostUpdateModelForm(instance=post)
    if request.method == 'POST':
        form = PostUpdateModelForm(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect('post_list')
        else:
            form = PostUpdateModelForm(instance=post)

    context = {'form': form}

    return render(request, 'update.html', context)

def post_delete_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    context = {'post': post}
    return render(request, 'delete.html', context)

def post_list_tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags=tag)
    context = {'title': f'Тег: {tag.name}',
               'posts': posts}
    return render(request, 'tags_list.html', context)