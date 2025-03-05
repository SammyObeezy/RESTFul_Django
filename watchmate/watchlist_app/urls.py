from django.urls import path, include
from watchlist_app.views import movie_list, movie_detail


urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>/', movie_detail, name='movie_detail'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name='stream-detail'),
]
