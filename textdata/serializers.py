from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

from textdata.models import Snippet, Tag


class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        password = make_password(validated_data['password'])
        mp_mater = User.objects.create(username=username, password=password)
        return validated_data

class viewListOfSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
class UpdateSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
class DeleteSnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'
class ListTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class tagDetailsSerializer(serializers.ModelSerializer):
    details = serializers.SerializerMethodField(source='get_details')
    class Meta:
        model = Tag
        fields = '__all__'

    def get_details(self, obj):

        try:
            datalist =[]
            snippet = Snippet.objects.filter(title = obj.id)
            for item in snippet:
                data = {
                    "user":item.user.username,
                    "timestamp":item.timestamp
                }
                datalist.append(data)

            return datalist
        except:
            data = {
                "user":"null",
                    "timestamp":"null"
            }
            return data
class totalCountListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = '__all__'



class addingSnippetSerializer(serializers.Serializer):

    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    username = serializers.CharField(required=False, allow_blank=True, max_length=100)
    timestamp = serializers.DateTimeField(required=False)


    def create(self, validated_data):
        title = validated_data['title']
        user = validated_data['username']
        timestamp = validated_data['timestamp']

        if Tag.objects.filter(title = title):
            tagId = Tag.objects.get(title=title).id
            Snippet.objects.create(title = Tag.objects.get(id=tagId),
                                    user = User.objects.get(id=user),
                                    timestamp = timestamp)
            return validated_data
        else:
            tags = Tag.objects.create(title=title)

            Snippet.objects.create(title=Tag.objects.get(id=tags.id),
                                   user=User.objects.get(id=user),
                                   timestamp=timestamp)
            return validated_data