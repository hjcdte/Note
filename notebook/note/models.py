from django.db import models
from django.conf import settings


class Note(models.Model):
    objects = models.Manager()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="单页所有人",
    )
    title = models.CharField("标题", max_length=50)
    content = models.TextField("内容")
    datetime = models.DateTimeField("修改时间")

    class Meta:
        verbose_name = "便签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + "-" + self.owner.username


class NoteTag(models.Model):
    objects = models.Manager()

    title = models.CharField("标签名", max_length=50)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class NoteAndNoteTag(models.Model):
    objects = models.Manager()

    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        verbose_name="便签",
    )

    note_tag = models.ForeignKey(
        NoteTag,
        on_delete=models.CASCADE,
        verbose_name="标签",
    )

    class Meta:
        verbose_name = "标签联系"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.note_tag.title + '-' + self.note.title


class Collections(models.Model):
    objects = models.Manager()

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="收藏所有人",
    )
    note = models.ForeignKey(
        Note,
        on_delete=models.CASCADE,
        verbose_name="便签",
    )
    datetime = models.DateTimeField("收藏时间")

    class Meta:
        verbose_name = "收藏便签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.note.title + "-" + self.owner.username
