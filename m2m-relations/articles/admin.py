from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Section, ArticleSection


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        set_common_section = False
        for form in self.forms:
            common_section = form.cleaned_data.get('common_section')
            if common_section:
                if set_common_section:
                    raise ValidationError('Основным разделом может быть только один!')
                set_common_section = True
        if not set_common_section:
            raise ValidationError('Укажите основной раздел!')
        return super().clean()


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    pass
