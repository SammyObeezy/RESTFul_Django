from django.urls import path, include
# from watchlist_app.views import movie_list, movie_detail
from watchlist_app.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAV.as_view, name='movie_detail'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]
