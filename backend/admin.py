from django.contrib import admin
from .models import User, UserImage, Tag, ProjectImage, Project, Skill, Experience


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link')
    inlines = [ProjectImageInline]
    search_fields = ('title', 'description')
    list_filter = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class UserImageInline(admin.TabularInline):
    model = UserImage
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    inlines = [UserImageInline, SkillInline, ExperienceInline]


admin.site.register(Tag, TagAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectImage)
admin.site.register(User, UserAdmin)
admin.site.register(UserImage)
admin.site.register(Skill)
admin.site.register(Experience)
