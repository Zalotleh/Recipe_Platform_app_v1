from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from recipe.views import *
from user.views import LoginUser
from user.views import profile

app_name = 'recipe'

urlpatterns = [
                  path('play-video/', play_video, name="play-video"),
                  path('', home, name='home_page'),
                  path("profile/", profile, name='user_profile'),
                  path("login/", LoginUser.as_view(), name='login'),
                  path('recipes-list', RecipeListView.as_view(), name='recipe_list'),
                  path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
                  path('recipe/create/', RecipeCreateView.as_view(), name='create_recipe'),
                  path('recipe/<int:pk>/update/', RecipeUpdateView.as_view(), name='update_recipe'),
                  path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='delete_recipe'),
                  path('about/', about, name='about'),
                  path('recipe/<int:pk>/add-comment', add_comment, name='add-comment'),
                  path('recipe/<int:pk>/delete-comment', comment_delete, name='delete-comment'),
                  path('like/<int:pk>', LikeView, name='like_recipe'),
                  path('add_category/', AddCategoryView.as_view(), name='add-category'),
                  path('category/<str:cats>/', CategoryView, name='category'),
                  path('category_list/', CategoryListView, name='category_list'),
                  path('search/', search, name='search_page'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
