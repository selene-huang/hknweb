from django.contrib import admin

from hknweb.polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']