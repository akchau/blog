from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin): # конфигурация отображения модели
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') # страницы которые отображаются в админке
    search_fields = ('text',) # поле по которому осуществляется поиск (может содержать только text, slug)
    list_filter = ('pub_date',) # фильтрация по дате
    empty_value_display = '-пусто-' # дефолтное значение пустого поля в админке


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description')
    list_editable = ('title', 'description',)
    search_fields = ('title','description',)
    empty_value_display = '-пусто-'



admin.site.register(Post, PostAdmin) # модель зарегестрированная тут будет показана в админке в разделе своего приложения
admin.site.register(Group, GroupAdmin)