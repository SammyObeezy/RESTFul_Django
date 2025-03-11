from rest_framework import serializers
from watchlist_app.models import MovieList

class WatchListSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
     
    class Meta:
        model = WatchList
        fields = "__all__"