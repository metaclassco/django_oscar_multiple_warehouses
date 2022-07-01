from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    partner = models.ForeignKey('partner.Partner', related_name='warehouses', on_delete=models.CASCADE)
    address = models.OneToOneField('address.WarehouseAddress', on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


from oscar.apps.partner.models import *  # noqa isort:skip
