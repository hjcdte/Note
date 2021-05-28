from django.urls import path
from . import views

urlpatterns = [
    path("notes", views.NoteListAPIView.as_view()),
    path("notes/<int:pk>", views.NoteDetailAPIView.as_view()),
    path("collections", views.CollectListAPIView.as_view()),
    path("tags", views.NoteTagListAPIView.as_view()),
    path("tags/<int:pk>", views.NoteTagDetailAPIView.as_view()),
    path("tagsAndnotes", views.NoteAndNoteTagListAPIView.as_view()),
    # path("user", views.UserAPIView.as_view()),
    # path('jwt', views.jwt.as_view())
]
