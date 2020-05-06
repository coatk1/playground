from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']

    # (title, fields)
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

    # From models.Question.__str__()
    # Displays headers
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Filter by pub_date
    list_filter = ['pub_date']

    # Filter by search
    search_fields = ['question_text']

# Register your models here.
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice) # using Inline above
