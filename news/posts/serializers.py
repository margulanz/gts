from rest_framework import serializers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "content",
            "tags",
            "category",
            "slug",
            "status",
            "pub_date",
            "edit_date"
        )
        read_only_fields = (
            "pub_date",
            "edit_date"
        )
    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)