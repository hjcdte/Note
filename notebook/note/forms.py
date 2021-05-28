# from django.forms import Form
# from django.forms import fields
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# from .models import Note


# class LoginForm(Form):
#     username = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "用户名不能为空",
#         },
#     )
#     password = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "密码不能为空",
#         },
#     )

#     def clean(self):
#         if (
#             User.objects.filter(
#                 username=self.cleaned_data.get("username")
#             ).exists()
#             == False
#         ):
#             msg = "用户名未注册"
#             self.add_error("username", msg)
#             return self.cleaned_data

#         if (
#             authenticate(
#                 username=self.cleaned_data.get("username"),
#                 password=self.cleaned_data.get("password"),
#             )
#             == None
#         ):
#             msg = "密码错误"
#             self.add_error("password", msg)

#         return self.cleaned_data


# class RegisterForm(Form):
#     username = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "用户名不能为空",
#         },
#     )
#     password1 = fields.CharField(
#         required=True,
#         min_length=8,
#         error_messages={
#             "required": "密码不能为空",
#             "min_length": "密码不能少于8位",
#         },
#     )
#     password2 = fields.CharField(
#         required=True,
#         min_length=8,
#         error_messages={
#             "required": "密码不能为空",
#             "min_length": "密码不能少于8位",
#         },
#     )
#     email = fields.EmailField(
#         required=True,
#         error_messages={
#             "required": "邮箱不能为空",
#             "invalid": "请输入一个有效的邮箱地址",
#         },
#     )

#     def clean(self):
#         if User.objects.filter(username=self.cleaned_data.get("username")):
#             msg = "用户名已被注册"
#             self.add_error("username", msg)

#         if self.cleaned_data.get("password2") != self.cleaned_data.get(
#             "password1"
#         ):
#             msg = "两次密码不一致！"
#             self.add_error("password2", msg)
#             # raise ValidationError('两次密码不一致！')

#         if User.objects.filter(email=self.cleaned_data.get("email")):
#             msg = "邮箱已被注册"
#             self.add_error("email", msg)

#         return self.cleaned_data


# class NoteAddForm(Form):
#     title = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "标题不能为空",
#         },
#     )

#     content = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "内容不能为空",
#         },
#     )


# class NotePutForm(Form):
#     id = fields.CharField(
#         required=True,
#     )

#     ownerid = fields.CharField(
#         required=True,
#     )

#     title = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "标题不能为空",
#         },
#     )

#     content = fields.CharField(
#         required=True,
#         error_messages={
#             "required": "内容不能为空",
#         },
#     )

#     def clean(self):
#         try:
#             note_id = int(self.cleaned_data.get("id")[0])
#         except:
#             msg = "无此便签"
#             self.add_error("id", msg)
#             return self.cleaned_data

#         if (
#             Note.objects.filter(owner=self.cleaned_data.get("ownerid"))
#             .filter(id=note_id)
#             .exists()
#             == False
#         ):

#             msg = "无此便签"
#             self.add_error("id", msg)

#         return self.cleaned_data


# class NoteGetForm(Form):
#     id = fields.CharField(
#         required=True,
#     )

#     ownerid = fields.CharField(
#         required=True,
#     )

#     def clean(self):

#         try:
#             note_id = int(self.cleaned_data.get("id"))
#         except:
#             msg = "无此便签"
#             self.add_error("id", msg)
#             return self.cleaned_data

#         if (
#             Note.objects.filter(owner=self.cleaned_data.get("ownerid"))
#             .filter(id=note_id)
#             .exists()
#             == False
#         ):

#             msg = "无此便签"
#             self.add_error("id", msg)

#         return self.cleaned_data


# class NoteDeleteForm(Form):
#     id = fields.CharField(
#         required=True,
#     )

#     ownerid = fields.CharField(
#         required=True,
#     )

#     def clean(self):

#         try:
#             note_id = int(self.cleaned_data.get("id"))
#         except:
#             msg = "无此便签"
#             self.add_error("id", msg)
#             return self.cleaned_data

#         if (
#             Note.objects.filter(owner=self.cleaned_data.get("ownerid"))
#             .filter(id=note_id)
#             .exists()
#             == False
#         ):

#             msg = "无此便签"
#             self.add_error("id", msg)

#         return self.cleaned_data
