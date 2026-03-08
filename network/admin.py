from django.contrib import admin
from .models import ElectronicsNetwork, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')
    search_fields = ('name', 'model')
    list_filter = ('release_date',)


# Действие для очистки задолженности
def clear_debt(modeladmin, request, queryset):
    """
    Admin action: очищает задолженность у выбранных объектов.
    """
    updated = queryset.update(debt=0.00)
    modeladmin.message_user(
        request,
        f'Задолженность успешно обнулена у {updated} объектов.'
    )


clear_debt.short_description = '🔹 Очистить задолженность у выбранных объектов'


@admin.register(ElectronicsNetwork)
class ElectronicsNetworkAdmin(admin.ModelAdmin):
    # 1. Отображение: добавлена ссылка на поставщика (supplier) через link_to_supplier
    list_display = (
        'id',
        'name',
        'level',
        'link_to_supplier',  # ← ссылка вместо текста
        'debt',
        'country',
        'city',
        'created_at'
    )

    # 2. Фильтр по городу
    list_filter = ('level', 'country', 'city', 'created_at')

    search_fields = ('name', 'email', 'city')

    readonly_fields = ('created_at',)

    # raw_id_fields = ('supplier',)

    filter_horizontal = ('products',)

    # 3. Добавляем действие "Очистить задолженность"
    actions = [clear_debt]

    fieldsets = (
        (None, {'fields': ('name', 'email')}),
        ('Адрес', {'fields': ('country', 'city', 'street', 'house_number')}),
        ('Иерархия', {'fields': ('supplier', 'level')}),
        ('Финансы', {'fields': ('debt',)}),
        ('Продукты', {'fields': ('products',)}),
        ('Системное', {'fields': ('created_at',), 'classes': ('collapse',)}),
    )

    def link_to_supplier(self, obj):
        """
        Показывает ссылку на поставщика в списке.
        """
        if not obj.supplier:
            return "—"
        url = f"/admin/network/electronicsnetwork/{obj.supplier.id}/change/"
        return f'<a href="{url}">{obj.supplier.name}</a>'

    link_to_supplier.allow_tags = True
    link_to_supplier.short_description = 'Поставщик'
    link_to_supplier.admin_order_field = 'supplier__name'  # сортировка по имени поставщика