from django.contrib import admin
from .models import Post, Group

class PostAdmin(admin.ModelAdmin): # конфигурация отображения модели
    list_display = ('pk', 'text', 'pub_date', 'author', 'group', 'image',) # страницы которые отображаются в админке
    search_fields = ('text',) # поле по которому осуществляется поиск (может содержать только text, slug)
    list_filter = ('pub_date',) # фильтрация по дате
    empty_value_display = '-пусто-' # дефолтное значение пустого поля в админке
    list_editable = ('text', 'group', 'image',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk','main_admin', 'image', 'title', 'slug', 'description')
    list_editable = ('main_admin','title', 'description', 'slug',)
    search_fields = ('title','description',)
    empty_value_display = '-пусто-'
    search_fields = ('title',)



admin.site.register(Post, PostAdmin) # модель зарегестрированная тут будет показана в админке в разделе своего приложения
admin.site.register(Group, GroupAdmin)
