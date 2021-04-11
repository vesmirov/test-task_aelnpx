from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError

User = get_user_model()


class Schema(models.Model):
    class Separator(models.TextChoices):
        COMMA = ',', 'Comma (,)'
        SEMICOLON = ';', 'Semicolon (;)'
        TAB = '\t', 'Tabulation'

    class QuoteChar(models.TextChoices):
        DQUOTE = '"', 'Double-quote (")'
        ASTERISK = '*', 'Asterisk (*)'
        VBAR = '|', 'Vertical bar (|)'
        CARET = '^', 'Caret (^)'

    user = models.ForeignKey(User,
        related_name='schemas',
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    title = models.CharField(max_length=75)
    separator = models.CharField(
        choices=Separator.choices,
        default=Separator.COMMA,
        max_length=20,
    )
    string_character = models.CharField(
        choices=QuoteChar.choices,
        default=QuoteChar.DQUOTE,
        max_length=20
    )

    class Meta:
        ordering = ('created',)
        verbose_name = 'schema'
        verbose_name_plural = 'schemas'

    def __str__(self):
        return self.title


class Column(models.Model):
    class ColumnType(models.TextChoices):
        FNAME = 'FNAME', 'Full name'
        JOB = 'JOB', 'Job'
        EMAIL = 'EMAIL', 'Email'
        DOMAIN = 'DOMAIN', 'Domain name'
        PHONE = 'PHONE', 'Phone number'
        COMPANY = 'COMPANY', 'Company name'
        TEXT = 'TEXT', 'Text'
        INTEGER = 'INTEGER', 'Integer'
        ADDRESS = 'ADDRESS', 'Address'
        DATE = 'DATE', 'Date'

    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(
        validators=[MaxValueValidator(100)]
    )
    column_type = models.CharField(
        verbose_name='Type',
        choices=ColumnType.choices,
        blank=False,
        max_length=50
    )
    integer_from = models.IntegerField('From', default=0)
    integer_to = models.IntegerField('To', default=0)
    text_len = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(500)]
    )
    schema = models.ForeignKey(
        Schema,
        blank=False,
        related_name='columns',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('order', '-created')
        verbose_name = 'column'
        verbose_name_plural = 'columns'

    @property
    def is_integer(self):
        return self.column_type == self.ColumnType.INTEGER
    
    @property
    def is_text(self):
        return self.column_type == self.ColumnType.TEXT

    def clean(self):
        if self.integer_from > self.integer_to:
            raise ValidationError('"To" can\'t be less than "From"')

    def __str__(self):
        return self.title
