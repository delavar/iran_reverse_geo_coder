from django.db import models

from utils.custom_fields import FarsiCharField, LocationField
from django.utils.translation import ugettext_lazy as _


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Province(models.Model):
    name = FarsiCharField(max_length=250, verbose_name=_("name"))
    description = models.TextField(verbose_name=_('Description'), blank=True)
    active = models.BooleanField(verbose_name=_('Active Status'), default=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        verbose_name = _("province")
        verbose_name_plural = _("provinces")

    def __str__(self):
        return self.name


class County(models.Model):
    name = FarsiCharField(max_length=250, verbose_name=_("name"))
    province = models.ForeignKey(Province, verbose_name=_("province"), null=True, on_delete=models.SET_NULL)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    active = models.BooleanField(verbose_name=_('Active Status'), default=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        verbose_name = _("county")
        verbose_name_plural = _("counties")

    def __str__(self):
        return self.name


class City(models.Model):
    name = FarsiCharField(max_length=250, verbose_name=_("name"))
    county = models.ForeignKey(County, verbose_name=_("county"), null=True, on_delete=models.SET_NULL)
    province = models.ForeignKey(Province, verbose_name=_("province"), null=True, on_delete=models.SET_NULL)
    lat = LocationField(verbose_name=_('Latitude'), blank=True, null=True)
    lng = LocationField(verbose_name=_('Longitude'), blank=True, null=True)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    active = models.BooleanField(verbose_name=_('Active Status'), default=True)

    objects = models.Manager()
    active_objects = ActiveManager()

    class Meta:
        verbose_name = _("city")
        verbose_name_plural = _("cities")

    def __str__(self):
        return self.name
