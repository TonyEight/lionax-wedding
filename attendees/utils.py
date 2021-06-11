from django.db import models
from django.conf import settings
from hashids import Hashids


def GetFieldsNameFromModel(model, add_many_to_many_fields=False, add_id=False):
    fields = []
    for field in model._meta.get_fields():
        if field.name == 'id':
            if not add_id:
                continue
        if isinstance(field, models.ManyToManyField) or \
           isinstance(field, models.ForeignKey) or \
           isinstance(field, models.ManyToManyRel) or \
           isinstance(field, models.ManyToOneRel):
            if not add_many_to_many_fields:
                continue
        fields.append(field.name)
    return fields


hashids = Hashids(settings.HASHIDS_SALT, min_length=20)


def h_encode(id):
    return hashids.encode(id)


def h_decode(h):
    z = hashids.decode(h)
    print(z)
    if z:
        print(z[0])
        return z[0]


class HashIdConverter:
    regex = '[a-zA-Z0-9]{20,}'

    def to_python(self, value):
        return h_decode(value)

    def to_url(self, value):
        return h_encode(value)
