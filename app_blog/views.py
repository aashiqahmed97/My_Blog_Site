from django.shortcuts import render , HttpResponseRedirect, redirect
from django.views.generic import CreateView , UpdateView , ListView , DetailView , DeleteView , View , TemplateView
from .models import Blog , comment , Likes
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
import uuid
from .forms import commentForm

# Create your views here.
class MyBlogs(LoginRequiredMixin , TemplateView):
    template_name ='app_blog/my_blogs.html'


class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['blog_title','blog_content','blog_image']
    template_name = 'app_blog/edit_blog.html'

    def get_success_url(self):
        return reverse_lazy('app_blog:blog_details', kwargs={'pk': self.object.pk})

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'app_blog/blog_list.html'
    


class createBlog(LoginRequiredMixin , CreateView):
    model = Blog
    template_name = 'app_blog/create_blog.html'
    fields = ['blog_title', 'blog_content', 'blog_image']

    def form_valid(self,form):
        blog_obj = form.save(commit=False)
        blog_obj.Author = self.request.user
        title = blog_obj.blog_title
        
        blog_obj.slug = slugify(blog_obj.blog_title)

        blog_obj.save()
        return redirect ('index')

def blog_details(request , pk ):
    blog = Blog.objects.get(id = pk)
    comment_form = commentForm
    already_liked =Likes.objects.filter(blog=blog, user = request.user)
    if already_liked:
        liked = True
    else:
        liked = False    
    if request.method == "POST":
        comment_form=commentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit = False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect('app_blog:blog_details', pk = blog.id )

    context ={'blog':blog ,'comment_form':comment_form, 'liked':liked}
    return render(request , 'app_blog/blog_details.html' , context)
@login_required
def liked(request , pk):
    blog = Blog.objects.get( id = pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    if not already_liked :
        liked_post= Likes(blog = blog, user = user)
        liked_post.save()
    return redirect ('app_blog:blog_details' , pk = blog.id )

@login_required
def unliked(request , pk):
    blog = Blog.objects.get( id = pk)
    user = request.user
    already_liked = Likes.objects.filter(blog=blog,user=user)
    already_liked.delete()
    return redirect ('app_blog:blog_details' , pk = blog.id )

