"""Assemble the public homepage payload from the content tables."""

from django.db.models import Prefetch

from content.models import ActionLink, HeroSlide, NavItem, PageSection, SiteSettings


def _file_url(request, file_field) -> str:
    if not file_field:
        return ""
    url = file_field.url
    if request is not None:
        return request.build_absolute_uri(url)
    return url


def _nav_node(item) -> dict:
    children = [
        _nav_node(child)
        for child in item.children.all()
        if child.is_active
    ]
    return {
        "id": item.id,
        "label": item.label,
        "url": item.url,
        "open_in_new_tab": item.open_in_new_tab,
        "children": children,
    }


def homepage_payload(request) -> dict:
    settings_row = SiteSettings.objects.first()
    if settings_row is None:
        site = {
            "university_line": "",
            "name_line": "",
            "equity_line": "",
            "logo_alt": "University of Global Health Equity",
            "logo_url": "",
            "search_placeholder": "Search",
            "show_search": True,
            "action_background_color": "#E6D4D8",
            "action_text_color": "#2C2426",
        }
    else:
        site = {
            "university_line": settings_row.university_line,
            "name_line": settings_row.name_line,
            "equity_line": settings_row.equity_line,
            "logo_alt": settings_row.logo_alt,
            "logo_url": _file_url(request, settings_row.logo_file) or settings_row.logo_url,
            "search_placeholder": settings_row.search_placeholder,
            "show_search": settings_row.show_search,
            "action_background_color": settings_row.action_background_color,
            "action_text_color": settings_row.action_text_color,
        }

    action_links = [
        {
            "id": link.id,
            "label": link.label,
            "url": link.url,
            "open_in_new_tab": link.open_in_new_tab,
        }
        for link in ActionLink.objects.filter(is_active=True)
    ]

    navigation = [
        _nav_node(item)
        for item in NavItem.objects.filter(parent__isnull=True, is_active=True).prefetch_related(
            Prefetch(
                "children",
                queryset=NavItem.objects.filter(is_active=True).order_by("position", "id"),
            )
        )
    ]

    slides = []
    for slide in HeroSlide.objects.filter(is_active=True):
        slides.append(
            {
                "id": slide.id,
                "media_type": slide.media_type,
                "media_url": _file_url(request, slide.file) or slide.external_url,
                "caption": slide.caption,
                "button_label": slide.button_label,
                "button_url": slide.button_url,
                "button_color": slide.button_color,
                "button_text_color": slide.button_text_color,
            }
        )

    sections = []
    for section in PageSection.objects.filter(is_active=True).prefetch_related("stats"):
        sections.append(
            {
                "id": section.id,
                "title": section.title,
                "stats": [
                    {
                        "id": stat.id,
                        "display_value": stat.display_value,
                        "description": stat.description,
                        "background_color": stat.background_color,
                        "text_color": stat.text_color,
                    }
                    for stat in section.stats.all()
                    if stat.is_active
                ],
            }
        )

    return {
        "site": site,
        "action_links": action_links,
        "navigation": navigation,
        "slides": slides,
        "sections": sections,
    }
