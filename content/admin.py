from django.contrib import admin

from content.models import ActionLink, HeroSlide, NavItem, PageSection, SiteSettings, Stat


class ChildNavInline(admin.TabularInline):
    model = NavItem
    fk_name = "parent"
    extra = 0
    fields = ("label", "url", "position", "is_active", "open_in_new_tab")
    ordering = ("position",)


class StatInline(admin.TabularInline):
    model = Stat
    extra = 0
    fields = (
        "display_value",
        "description",
        "background_color",
        "text_color",
        "position",
        "is_active",
    )
    ordering = ("position",)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Wordmark",
            {
                "fields": (
                    "university_line",
                    "name_line",
                    "equity_line",
                    "logo_alt",
                    "logo_file",
                    "logo_url",
                )
            },
        ),
        (
            "Header actions",
            {
                "fields": (
                    "show_search",
                    "search_placeholder",
                    "action_background_color",
                    "action_text_color",
                )
            },
        ),
    )

    def has_add_permission(self, request):
        if SiteSettings.objects.exists():
            return False
        return super().has_add_permission(request)


@admin.register(ActionLink)
class ActionLinkAdmin(admin.ModelAdmin):
    list_display = ("label", "url", "position", "is_active", "open_in_new_tab")
    list_editable = ("position", "is_active")
    ordering = ("position",)


@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ("label", "parent", "url", "position", "is_active")
    list_editable = ("position", "is_active")
    list_filter = ("is_active", "parent")
    search_fields = ("label", "url")
    ordering = ("position",)

    def get_inlines(self, request, obj):
        if obj is None or obj.parent_id is not None:
            return []
        return [ChildNavInline]


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ("__str__", "media_type", "position", "is_active")
    list_editable = ("position", "is_active")
    list_filter = ("media_type", "is_active")
    ordering = ("position",)
    fieldsets = (
        ("Media", {"fields": ("media_type", "file", "external_url", "is_active", "position")}),
        ("Caption", {"fields": ("caption",)}),
        (
            "Button",
            {
                "fields": (
                    "button_label",
                    "button_url",
                    "button_color",
                    "button_text_color",
                )
            },
        ),
    )


@admin.register(PageSection)
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "position", "is_active")
    list_editable = ("position", "is_active")
    inlines = [StatInline]


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ("display_value", "section", "position", "is_active")
    list_editable = ("position", "is_active")
    list_filter = ("section", "is_active")
    ordering = ("section", "position")
