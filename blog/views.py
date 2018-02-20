from django.utils import timezone
from .models import Post, Publication, UserProfile
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, PublicationForm, UserProfileForm
from django.shortcuts import redirect


def home(request):
    workers = UserProfile.objects.filter()
    for worker in workers:
        words = worker.info.split()
        if len(words) > 15:
            worker.info = " ".join(words[:15]) + " "

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    for post in posts:
        words = post.text.split()
        if len(words) > 50:
            post.text = " ".join(words[:50]) + " "

    return render(request, 'blog/home.html', {'workers': workers, 'posts': posts})


def publications(request, worker_id):
    publications = Publication.objects.filter(author_id=worker_id).order_by('publication_date').reverse()
    for publication in publications:
        words = publication.title.split()
        if len(words) > 50:
            publication.title = " ".join(words[:50]) + " "
    return render(request, 'blog/publications.html', {'publications': publications})


def publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'blog/published.html', {'publication': publication})


def worker(request, pk):
    worker = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'blog/worker.html', 'blog/publications.html', {'worker': worker})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, files=request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
