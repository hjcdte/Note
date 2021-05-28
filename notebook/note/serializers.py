import pickle

from django.db.models import fields
from django.db.models import Count
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import (
    Note,
    Collections,
    NoteTag,
    NoteAndNoteTag,
)
from rest_framework.authentication import SessionAuthentication
from .tasks import serialize_create_task


class NoteListSerializer(serializers.ModelSerializer):
    collected_count = serializers.SerializerMethodField(read_only=True)
    tag_title = serializers.SerializerMethodField(read_only=True)

    def get_collected_count(self, obj):
        # count = obj.objects.annotate(collects=Count('collections'))
        # 一条sql搞出来
        if hasattr(obj, "collects"):
            return obj.collects
        return 0

    def get_tag_title(self, obj):
        tag_title = obj.noteandnotetag_set.all()

        if(len(tag_title) == 0):
            return 0

        return [{'title':i.note_tag.title, 'id':i.note_tag.id} for i in tag_title]

    class Meta:
        model = Note
        fields = "__all__"


class NoteTagListSerializer(serializers.ModelSerializer):
    belong_count = serializers.SerializerMethodField(read_only=True)

    def get_belong_count(self, obj):
        # count = obj.objects.annotate(collects=Count('collections'))
        # 一条sql搞出来
        if hasattr(obj, "belongs"):
            return obj.belongs
        return 0

    class Meta:
        model = NoteTag
        fields = "__all__"


class NoteAndNoteTagListSerializer(serializers.ModelSerializer):
    note_title = serializers.SerializerMethodField(read_only=True)
    note_tag_title = serializers.SerializerMethodField(read_only=True)

    def get_note_title(self, obj):
        return obj.note.title

    def get_note_tag_title(self, obj):
        return obj.note_tag.title

    class Meta:
        model = NoteAndNoteTag
        fields = '__all__'


class CollectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = "__all__"

    def create(self, validated_data):
        data = pickle.dumps(validated_data)
        serialize_create_task.delay(data)

        return validated_data
# class UserSerialize(serializers.ModelSerializer):
#
#     password_confirm = serializers.CharField(label="确认密码", write_only=True)
#
#     def create(self, validated_data):
#
#         return print(validated_data)
#
#     def validate(self, data):
#         print(data)
#         if User.objects.filter(username=data.get("username")):
#             raise serializers.ValidationError({"username": "用户名已注册"})
#         if data.get("password") != data.get("password_confirm"):
#             raise serializers.ValidationError({"password_confirm": "两次密码不一样"})
#         return data
#
#     class Meta:
#         model = User
#         fields = ("username", "password", "password_confirm", "email")
