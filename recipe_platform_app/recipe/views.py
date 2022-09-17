from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View,ListView, UpdateView, DeleteView, CreateView
from store.models import Products
from .forms import CommentForm
from .mixins import YouTube
from .models import *
from hitcount.views import HitCountDetailView




def home(request):
    return render(request, 'recipes/index.html', {})


def about(request):
    return render(request, 'recipes/about.html', {'title': 'about page'})


def play_video(request):
    vid_id = request.GET.get("vid_id")

    vid_data = YouTube(vid_id=vid_id).get_video()

    context = {
        "vid_data": vid_data,
    }
    return render(request, 'recipes/play_video.html', context)


class RecipeListView(ListView):
    template_name = 'recipes/recipes_list.html'
    model = Recipe
    context_object_name = 'recipes'


class RecipeDetailView(HitCountDetailView):
    template_name = 'recipes/recipe_detail.html'
    model = Recipe
    count_hit = True

    def get_context_data(self, **kwargs):
        recipe = Recipe.objects.get(pk=self.object.pk)

        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        context['num_comments'] = Comment.objects.filter(recipe=recipe).count()
        context['total_likes'] = recipe.total_likes()
        return context


class RecipeUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'recipes/update_recipe.html'
    model = Recipe
    success_url = reverse_lazy('recipe:recipe_list')
    fields = ['title', 'category', 'description', 'ingredients',
              'number_of_portions', 'preparation_time', 'total_time',
              'video', 'external_video']
    permission_required = "recipe.change_recipe"

    # only the author of the recipe is allowed to update it
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeCreateView(LoginRequiredMixin, CreateView):
    template_name = 'recipes/create_recipe.html'
    model = Recipe
    success_url = reverse_lazy('recipe_list')
    fields = ['title', 'description', 'ingredients', 'number_of_portions',
              'preparation_time', 'total_time', 'video',
              'external_video']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class RecipeDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'recipes/delete_recipe.html'
    model = Recipe
    success_url = reverse_lazy('home_page')
    permission_required = "recipe.delete_recipe"

    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


class AddCategoryView(PermissionRequiredMixin, CreateView):
    model = Category
    template_name = 'recipes/add_category.html'
    fields = '__all__'
    permission_required = 'add_category'


def CategoryView(request, cats):
    category_recipes = Recipe.objects.filter(category=cats.title())

    return render(request, 'recipes/categories.html',
                  {'cats': cats, 'category_recipes': category_recipes})


def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'recipes/category_list.html',
                  {'cat_menu_list': cat_menu_list})


def add_comment(request, pk):
    # on click at add comment, will take the formation from db for the particular recipe

    recipe = Recipe.objects.get(id=pk)

    if request.method == 'POST':
        # if the request is POST will take all the info related to that recipe form

        form = CommentForm(request.POST, instance=recipe)
        if form.is_valid():
            name = request.user
            body = form.cleaned_data['comment_body']
            # and we save the comment info

            c = Comment(recipe=recipe, commenter_name=name,
                        comment_body=body, date_added=datetime.now())
            c.save()
            return redirect(reverse('recipe:recipe_detail', args=[recipe.pk]))

    else:
        form = CommentForm()

    context = {
        'form': form,
    }

    return render(request, 'recipes/add_comment.html', context)


@login_required
def comment_delete(request, pk):
    Comment.objects.get(pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def LikeView(request, pk):
    recipe = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    recipe.likes.add(request.user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search(request):
    if request.method == 'POST':
        searched = request.POST.get('searched')
        recipes = Recipe.objects.filter(title__icontains=searched)
        categories = Category.objects.filter(name__icontains=searched)
        products = Products.objects.filter(name__icontains=searched)
        context = {
            'searched': searched,
            'recipes': recipes,
            'categories': categories,
            'products': products,
        }
        return render(request, 'recipes/search.html', context
                      )
    else:
        return render(request, 'recipes/search.html', {})
