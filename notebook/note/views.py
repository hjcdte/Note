from rest_framework import (
	generics,
    filters,
)
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count
import pickle
import shelve
from .models import (
    Note,
    Collections,
    NoteTag,
    NoteAndNoteTag,
)
from .serializers import (
    NoteListSerializer,
    CollectListSerializer,
    NoteTagListSerializer,
    NoteAndNoteTagListSerializer,
    # UserSerialize,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class NoteListAPIView(generics.ListCreateAPIView):
    serializer_class = NoteListSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('id', 'title', 'content')
    search_fields = ('title', 'content')
    #?search= title or content
    ordering_fields = ('datetime',)

    def get_queryset(self):
        # notes = Note.objects.all().annotate(collects=Count('collections'))
        # notes = Note.objects.filter(owner=self.request.user).annotate(
        #     collects=Count("collections")
        # )
        notes = Note.objects.all().annotate(
			collects=Count("collections")
		)

        return notes


class NoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteListSerializer

    def get_queryset(self):
        notes = Note.objects.all().annotate(
			collects=Count("collections")
		)

        return notes


class NoteTagListAPIView(generics.ListCreateAPIView):
    serializer_class = NoteTagListSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ('title',)
    search_fields = ('title',)
    ordering_fields = ('id',)

    def get_queryset(self):
        tags = NoteTag.objects.all().annotate(
            belongs=Count("noteandnotetag")
        )

        return tags


class NoteTagDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteTagListSerializer

    def get_queryset(self):
        tags = NoteTag.objects.all().annotate(
            belongs=Count("noteandnotetag")
        )

        return tags


class NoteAndNoteTagListAPIView(generics.ListCreateAPIView):
    queryset = NoteAndNoteTag.objects.all()
    serializer_class = NoteAndNoteTagListSerializer
    #
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('note_tag',)


class CollectListAPIView(generics.ListCreateAPIView):
    queryset = Collections.objects.all()
    serializer_class = CollectListSerializer

    # def create(self, request, *args, **kwargs):
    #     task_data = {
    #         'request': request.__class__,
    #         'my_class': self.__class__,
    #         'request_data': request.data,
    #     }
    #     task_data = pickle.dumps(task_data)
    #     perform_create_task.delay(task_data)
    #
    #     return Response({}, status=status.HTTP_201_CREATED, headers={})

    # def perform_create(self, serializer):
    #     with shelve.open('serializer_db') as serializer_data:
    #         serializer_data['serializer'] = serializer
    #     perform_create_task.delay()
# class UserAPIView(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerialize
