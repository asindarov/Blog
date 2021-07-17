from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Article(models.Model):
	title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Article's title")
	content = RichTextUploadingField(blank=True, null=True)
	slug = models.SlugField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True, verbose_name='date of created')


	def save(self):
		self.slug = slugify(self.title)
		super(Article, self).save()
	def __str__(self):
		return self.slug	

	class Meta:
		ordering = ['-created_date']	





def get_topbanner_filename(instance, filename):
    title = instance.title
    slug = slugify(title)
    return "documents/banner/{}/{}".format(slug, filename)



def get_image_filename(instance, filename):
    title = instance.blog.id
    slug = slugify(title)
    return "post_images/post_images_{}/{}".format(slug, filename)


def get_user_image_filename(instance, filename):
    title = instance.author
    slug = slugify(title)
    return "user_image_{}/{}".format(slug, filename)
