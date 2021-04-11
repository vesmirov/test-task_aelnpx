from django import forms

from schemas.models import Schema, Column


class SchemaForm(forms.ModelForm):
    class Meta:
        model = Schema
        fields = ('title', 'separator', 'string_character')
        labels = {
            'title': 'Name',
            'separator': 'Column separator',
            'string_character': 'String character',
        }

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = (
            'title',
            'column_type',
            'integer_from',
            'integer_to',
            'text_len',
            'order',
        )
        labels = {
            'title': 'Column name',
            'column_type': 'Value type',
            'integer_from': 'From',
            'integer_to': 'To',
            'text_len': 'Sentences',
            'order': 'Column order',
        }
        help_texts = {
            'column_type': 'For Integer: specify range<br>'
                           'For Text: specify the number of sentences'
        }
