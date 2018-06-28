from django.conf import settings
from django.urls import reverse
from django.db import models
from django_summernote import models as summer_model
from django_summernote import fields as summer_fields



class Constructionpost(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(blank=True, upload_to="uploads/%Y/%m/%d")
    # 저장경로 : MEDIA_ROOT/blog/2017/05/10/xxxx.jpg 경로에 저장
    # DB필드 : 'MEDIA_URL/blog/2017/05/10/xxxx.jpg' 문자열 저장



class Post(summer_model.Attachment):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
	title = models.CharField(max_length=200)
	content = summer_fields.SummernoteTextField(default='')
	created_at = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		ordering = ['-created_at']

	def get_absolute_url(self):
		return reverse('waterapp:post_detail', args=[self.id])

	def __str__(self):
		return self.title