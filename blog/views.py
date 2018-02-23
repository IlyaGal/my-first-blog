from django.utils import timezone
from django.views.generic import TemplateView

from .models import Post, Publication, UserProfile, PageWithTests
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, PublicationForm, UserProfileForm, PageWithTestsForm
from django.shortcuts import redirect


class Cooperation(TemplateView):
    template_name = 'blog/home_cooperation.html'


def home(request):
    workers = UserProfile.objects.order_by('hierarchy')
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
    rabotnik = UserProfile.objects.get(user_id=worker_id)
    return render(request, 'blog/publications.html', {'publications': publications, 'worker': rabotnik})


def publication(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    return render(request, 'blog/publication.html', {'publication': publication})


def pageWithTests(request, worker_id):
    print("ya zashol v pageWithTests")
    print(worker_id)
    pageWithTests = PageWithTests.objects.filter(author_id=worker_id).order_by('publication_date')
    print("vnurti pageWithTests labyda: {}".format(pageWithTests))
    rabotnik = UserProfile.objects.get(user_id=worker_id)
    return render(request, 'blog/pageWithTests.html', {'pageWithTests': pageWithTests, 'worker': rabotnik})


def pageWithTest(request, pk):
    pageWithTest = get_object_or_404(PageWithTests, pk=pk)
    return render(request, 'blog/pageWithTest.html', {'pageWithTest': pageWithTest})


def worker(request, pk):
    worker = get_object_or_404(UserProfile, pk=pk)
    return render(request, 'blog/worker.html', {'worker': worker})


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
