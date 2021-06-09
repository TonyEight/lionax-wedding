from django.db import models


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
