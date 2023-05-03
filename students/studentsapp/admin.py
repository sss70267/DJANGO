from django.contrib import admin
from studentsapp.models import student

class studentAdmin(admin.ModelAdmin):
    #加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
	list_filter=('cName','cSex')
	search_fields=('cName',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)
	
# Register your models here.
