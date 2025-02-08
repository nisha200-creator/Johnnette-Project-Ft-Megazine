from django.contrib import admin
from . models import Category,Megazine,Crd,FeaturedPost, LeftContent



class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'created_at', 'updated_at')


class MegazineAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'auther', 'magazine_img', 'short_desc', 'magazine_body', 'status', 'is_featured', 'updated_at')

    search_fields =('id','title','category__category_name')

    list_editable =('is_featured',  )


# class MustReadAdmin (admin.ModelAdmin):

#     list_display = ('title', 'image','link')


class CardsAdmin(admin.ModelAdmin):
    list_display = ('title','short_desc', 'image', 'link', 'updated_at')
    search_fields = ('title',)  
    list_filter = ('updated_at',)  



class FeaturedPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date', 'link')
    search_fields = ('title', 'category', 'description')


class LeftContentAdmin(admin.ModelAdmin):
    list_display=('title','image','short_desc','updated_at')
    search_fields = ('title' , )









admin.site.register(Category,categoryAdmin)
admin.site.register(Megazine, MegazineAdmin)
admin.site.register(Crd,CardsAdmin )
admin.site.register(FeaturedPost,FeaturedPostAdmin)
admin.site.register(LeftContent,LeftContentAdmin)


# Register your models here.
