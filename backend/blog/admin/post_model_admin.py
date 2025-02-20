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
    list_display = (
        'post_id',
        'title',
        'publish_date',
        'created_at',
        'is_public',
        'is_draft',
    )
    list_display_links = (
        'title',
    )
    list_editable = (
        'publish_date',
        'is_public',
        'is_draft',
    )
    ordering = (
        '-post_id',
    )



# For Emacs
# Local Variables:
# coding: utf-8
# End:
# post_model_admin.py ends here
