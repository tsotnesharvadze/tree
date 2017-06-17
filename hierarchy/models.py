from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import ugettext_lazy as _
from versatileimagefield.fields import VersatileImageField,PPOIField

class AbsTime(models.Model):
	created = models.DateTimeField(_('შეიქმნა'), auto_now_add=True, null=True)
	updated = models.DateTimeField(_('განახლდა'), auto_now=True, null=True)

	class Meta:
		abstract = True


class PersonModel(AbsTime):
    SEX=(('0',_('ქალი'),),
         ('1',_('კაცი'),))
    name = models.CharField(verbose_name=_('სახელი'),max_length=40,null=True,blank=True)
    lastname = models.CharField(verbose_name=_('გვარი'),max_length=40,null=True,blank=True)
    sex = models.CharField(verbose_name=_('გვარი'),max_length=1,choices=SEX)
    born_date = models.DateTimeField(_('დაბადების თარიღი'), null = True, blank=True)
    death_date = models.DateTimeField(_('გარდაცვალების თარიღი'), null = True, blank=True)
    wife = models.ForeignKey("PersonModel",verbose_name=_('მეუღლე'),blank=True, null=True,related_name='wife_set')
    children = models.ForeignKey("PersonModel",verbose_name=_('შვილები'),blank=True, null=True,related_name='children_set')
    dossier = RichTextUploadingField(verbose_name='დოსიე',blank=True, null=True)
    image = VersatileImageField(verbose_name='სურათი',blank=True, null=True,upload_to='prof_imgs/',ppoi_field='ppoi')
    ppoi = PPOIField(
        'სურათი'
    )

    def get_full_name(self):
        return self.name+' '+self.lastname

    def __str__(self):
        return self.get_full_name()

    def have_children(self):
        return self.children_set.count()>0 and self.sex == '1'

    def get_children(self):
        return self.children_set.all()

    class Meta:
        verbose_name='პიროვნება'
        verbose_name_plural='პიროვნებები'