from django.contrib import admin
from .models import Quiz


# Register your models here.
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ("formatted_prompt_response", "user_id", "solved_at")

    def formatted_prompt_response(self, obj):
        return f"{obj.prompt}: {obj.response}"

    formatted_prompt_response.short_description = "문제: 답"
