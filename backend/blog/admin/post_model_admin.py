#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""post_model_admin --

"""
from django_summernote.admin import SummernoteModelAdmin


class PostModelAdmin(SummernoteModelAdmin):
    """PostModelAdmin

    PostModelAdmin is a SummernoteModelAdmin.
    Responsibility:
    """
    summernote_fields = ('content', )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_model_admin.py ends here
