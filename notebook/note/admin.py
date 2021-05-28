from django.contrib import admin
from .models import (
    Note,
    Collections,
    NoteTag,
    NoteAndNoteTag,
)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("owner_username", "title", "datetime")
    ordering = ("title", "datetime")

    def owner_username(self, obj):
        return obj.owner.username

    owner_username.short_description = "便签所有人"


@admin.register(NoteTag)
class NoteTagAdmin(admin.ModelAdmin):
    list_display = ("title", "note_title",)
    ordering = ("title",)

    def note_title(self, obj):
        return obj.note.title

    note_title.short_description = "便签标题"


@admin.register(NoteAndNoteTag)
class NoteAndNoteTagAdmin(admin.ModelAdmin):
    list_display = ("note_tag_title", "note_title",)

    def note_tag_title(self, obj):
        return obj.note_tag.title

    def note_title(self, obj):
        return obj.note.title

    note_tag_title.short_description = "标签"

    note_title.short_description = "便签"


@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ("owner_username", "note_title", "datetime")
    ordering = ("datetime",)

    def owner_username(self, obj):
        return obj.owner.username

    owner_username.short_description = "便签所有人"

    def note_title(self, obj):
        return obj.note.title

    note_title.short_description = "便签标题"
