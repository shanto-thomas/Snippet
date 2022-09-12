from django.shortcuts import render
from rest_framework import viewsets, status, permissions

from django.contrib.auth.models import User
from rest_framework.response import Response

from snippet.settings import apis
from textdata.models import Snippet, Tag
from textdata.serializers import RegisterUserSerializer, addingSnippetSerializer, viewListOfSnippetSerializer, \
    UpdateSnippetSerializer, DeleteSnippetSerializer, ListTagSerializer, tagDetailsSerializer, totalCountListSerializer


# Create your views here.


class RegisterusersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added ', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)
class addingSnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to add items.
    """
    queryset = Snippet.objects.all()
    serializer_class = addingSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added ', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)
class viewListOfSnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view list of items.
    """
    queryset = Snippet.objects.all()
    serializer_class = viewListOfSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"promptmsg": "Something missing"}, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({'promptmsg': 'Sucessfully added ', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        headers=headers)
class UpdateSnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to edit the item.
    """
    queryset = Snippet.objects.all()
    serializer_class = UpdateSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):

        # print("hiii")
        instance = self.get_object()
        instance.title =Tag.objects.get(id= request.data.get("title"))
        instance.user = User.objects.get(id=request.data.get("user"))
        instance.timestamp = request.data.get("timestamp")
        # print(instance)
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({'promptmsg': 'Successfully Updated', 'data': serializer.data},
                        status=status.HTTP_201_CREATED,
                        )
class DeleteSnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be delete item.
    """
    queryset = Snippet.objects.all()
    serializer_class = DeleteSnippetSerializer
    permission_classes = [permissions.IsAuthenticated]


class ListTagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view the tag.
    """
    queryset = Tag.objects.all()
    serializer_class = ListTagSerializer
    permission_classes = [permissions.IsAuthenticated]


class tagDetailsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to view the details of tag
    """
    queryset = Tag.objects.all()
    serializer_class = tagDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

class totalCountListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be view total count.
    """
    queryset = Snippet.objects.all()
    serializer_class = totalCountListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):

        count = Snippet.objects.all().count()
        datalist =[]
        snippet = Snippet.objects.all()

        for item in snippet:
            data={
                "details":apis+str(item.title.id)
            }
            datalist.append(data)

        return Response({"count": count,"detailsSnippet":datalist})

