from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Post,PostManager
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):

    cont = {
        'posts': posts,
        'recent_posts': recent_posts,
    }
    return render(request, 'home.html', cont)

###Lising the posts	
class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5
	
###listing each post details
class DetailListView(DetailView):
	model = Post
	template_name = 'blog/post_detail.html'

##create new posts
class CreateListView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title', 'content']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
		
##Update posts...
class UpdateListView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title', 'content']
	
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		else:
			print('Cant update other posts')
			return False
		
		
		
class DeleteListView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post
	success_url = '/'
	template_name = 'blog/post_confirm_delete.html'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False
		
	
def about(request):
	return render(request, 'blog/about.html')

def disclaimer(request):
	return HttpResponse('<h1>Blog Disclaimer</h1>')
	
def contactus(request):
	return HttpResponse('<h1>Blog Contact US</h1>')

