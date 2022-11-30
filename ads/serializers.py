from rest_framework import serializers

from ads.models import Ad, Comment

"""
pk": 0,
"text": "string",
"author_id": 0,
"created_at": "2019-08-24T14:15:22Z",
"author_first_name": "string",
"author_last_name": "string",
"ad_id": 0,
"author_image": "http://example.com"
}
"""


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.pk')
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    ad_id = serializers.ReadOnlyField(source='ad.pk')
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = ['pk',
                  'text',
                  'author_id',
                  'created_at',
                  'author_first_name',
                  'author_last_name',
                  'ad_id',
                  'author_image']


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ['pk', 'price', 'image', 'description', 'title']


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')
    phone = serializers.CharField(source="author.phone", required=False, read_only=True)

    class Meta:
        model = Ad
        fields = ['pk',
                  'image',
                  'title',
                  'price',
                  'phone',
                  'description',
                  'author_first_name',
                  'author_last_name',
                  'author_id']
