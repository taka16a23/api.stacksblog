#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""recursive_field -- recursive field serializer

"""
from rest_framework import serializers


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# recursive_field.py ends here
