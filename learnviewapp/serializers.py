from rest_framework import serializers
from learnviewapp.models import PostMedia

class PostMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostMedia
        fields = '__all__'
        
