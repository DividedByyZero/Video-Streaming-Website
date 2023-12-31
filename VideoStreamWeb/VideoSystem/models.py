from django.db import models
from django.contrib.auth.models import User

class VideoUpload(models.Model):
    Upload_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='uploader_name')
    Video_title = models.CharField(max_length = 256,verbose_name="Put Your Video Title")
    Upload_Thumbnail = models.ImageField(upload_to='thumbnails')
    Upload_video = models.FileField(upload_to='videos', null=True, verbose_name="Upload Your Video")
    slug = models.SlugField(max_length = 264,unique=True)
    Video_description = models.CharField(max_length = 1000, verbose_name = "Give a description :")
    Upload_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Video_title

class VideoComment(models.Model):
    TheVideo = models.ForeignKey(VideoUpload,on_delete=models.CASCADE,related_name = 'video_name')
    TheUser = models.ForeignKey(User,on_delete = models.CASCADE,related_name='commenter')
    comment = models.TextField()
    Comment_date = models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return self.comment
