#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""base_model_form -- base model form

"""
from django import forms
from base import medias


class BaseModelForm(forms.ModelForm):
    """BaseModelForm

    BaseModelForm is a forms.ModelForm.
    Responsibility:
    """

    # override
    @property
    def media(self, ):
        media = super(BaseModelForm, self).media
        media = medias.BASE_ADMIN_MEDIA + media
        return media



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# base_model_form.py ends here
