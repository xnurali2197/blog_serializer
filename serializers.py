class BlogSerializer(serializers.ModelSerializer):
    short_content = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'short_content']

    def get_short_content(self, obj):
        return obj.content[:50]
