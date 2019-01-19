from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from blog_app.forms import PostForm,CommentForm,ProfileForm
from blog_app.models import Post,Comment,Friend,UserProfileInfo
from django.contrib.auth.models import User

# Create your views here.


class AboutView(TemplateView):
    template_name = "about.html"

class ListUser(ListView):
    model = User
    template_name = 'list_user.html'

class PostList(ListView):
    model = Post
    template_name = "post_list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(PostList, self).get_context_data(*args, **kwargs)
        usr = User.objects.get(username=self.request.user.username)
        friendss = Friend.objects.get(current_user=usr)
        context['friends'] = friendss.users.all()
        return context


class BlogPost(DetailView):
    model = Post
    template_name = "post_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(BlogPost, self).get_context_data(*args, **kwargs)
        usr = get_object_or_404(Post,pk=self.kwargs["pk"])
        comment = Comment.objects.filter(post=usr)
        context['comment'] = comment.all()
        return context

class CreatePost(CreateView):
    template_name = "post_form.html"
    form_class = PostForm
    model=Post
    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return redirect("blog_app:post_list")



class BlogUpdate(LoginRequiredMixin,UpdateView):
        login_url = '/login/'
        redirect_field_name = 'blog_app/post_detail.html'
        form_class = PostForm
        template_name = "post_form.html"
        model=Post
        def form_valid(self, form):
            self.object=form.save(commit=False)
            self.object.author = self.request.user
            self.object.save()
            return redirect("blog_app:post_list")


class PostDelete(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


class DraftList(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog_app/post_list.html'
    model = Post

    def get_queryset(self):
        return Post.object.filter(published_date__isnull=True.order_by('created_date'))



@login_required
def add_comment_to_post(request,pk):
    post_com = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form_c = CommentForm(request.POST)
        if form_c.is_valid():
            form_comments = form_c.save(commit=False)
            form_comments.post = post_com
            form_comments.save()
            return redirect ('blog_app:blog_post',post_com.pk)
    else:
        form_c = CommentForm()
    return render(request,'blog_app/comments_form.html',{'form':form_c})


@login_required
def comment_approval(request,pk):
    comments = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect ('blog_post',comments.post.pk)

@login_required
def comment_delete(request,pk):
    comments = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect ('blog_post',pk=post_pk)


@login_required
def publish_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect("blog_app:post_list")


@login_required
def add_friend(request,pk):
    login_user = request.user
    usr = get_object_or_404(User,pk=pk)
    friend = Friend.objects.get_or_create(current_user=login_user)
    friend[0].users.add(usr)
    friend2 = Friend.objects.get_or_create(current_user=usr)
    friend2[0].users.add(login_user)
    return redirect("blog_app:list_user")

def friend_list(request,pk):
    usr = get_object_or_404(User,pk=pk)
    friend = Friend.objects.get(current_user=usr)
    fs = friend.users.all()
    return render(request,'blog_app/friend_list.html',{'frnds':fs})


def user_profile(request,pk):
    usr = User.objects.get(pk=pk)
    try:
        pp = request.user.userprofileinfo
    except UserProfileInfo.DoesNotExist:
        pp = UserProfileInfo(user_p=request.user)

    if request.method == 'POST':
        form_t1 = ProfileForm(request.POST,request.FILES ,instance=pp)
        if form_t1.is_valid():
            temp = form_t1.save(commit=False)
            temp.user_p = usr
            temp.save()
    else:
        form_t1 = ProfileForm(instance=pp)
    return render(request,'blog_app/user_profile.html',{ 'pp' : pp , 'form_1' : form_t1 , 'user' : usr })
