from django.core.exceptions import ValidationError
from django.db import models


class SiteSettings(models.Model):
    """Singleton row for the header chrome: logo, colours, and search."""

    university_line = models.CharField(max_length=80, default="UNIVERSITY OF")
    name_line = models.CharField(max_length=80, default="Global Health")
    equity_line = models.CharField(max_length=80, default="EQUITY")
    logo_alt = models.CharField(
        max_length=160,
        default="University of Global Health Equity",
    )
    logo_file = models.ImageField(upload_to="branding/", blank=True)
    logo_url = models.URLField(
        blank=True,
        help_text="Used when no logo file is uploaded.",
    )
    search_placeholder = models.CharField(max_length=80, default="Search")
    show_search = models.BooleanField(default=True)
    action_background_color = models.CharField(max_length=20, default="#E6D4D8")
    action_text_color = models.CharField(max_length=20, default="#2C2426")
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Site settings"
        verbose_name_plural = "Site settings"

    def __str__(self) -> str:
        return self.logo_alt


class ActionLink(models.Model):
    """Top-right buttons such as Apply and Get Involved."""

    label = models.CharField(max_length=80)
    url = models.URLField()
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return self.label


class NavItem(models.Model):
    """Primary navigation item. Leave the URL empty when it only opens a menu."""

    label = models.CharField(max_length=120)
    url = models.CharField(max_length=500, blank=True)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    open_in_new_tab = models.BooleanField(default=False)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        if self.parent_id:
            return f"{self.parent} / {self.label}"
        return self.label


class HeroSlide(models.Model):
    """One frame of the homepage slideshow. A frame is an image or a video."""

    IMAGE = "image"
    VIDEO = "video"
    MEDIA_CHOICES = [
        (IMAGE, "Image"),
        (VIDEO, "Video"),
    ]

    media_type = models.CharField(max_length=10, choices=MEDIA_CHOICES, default=IMAGE)
    file = models.FileField(
        upload_to="slides/",
        blank=True,
        help_text="Optional upload. A file is shown instead of the external URL.",
    )
    external_url = models.URLField(
        blank=True,
        help_text="Image URL, direct video file, or a YouTube link.",
    )
    caption = models.TextField()
    button_label = models.CharField(max_length=80, blank=True)
    button_url = models.URLField(blank=True)
    button_color = models.CharField(max_length=20, default="#79B9BC")
    button_text_color = models.CharField(max_length=20, default="#FFFFFF")
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return f"{self.get_media_type_display()}: {self.caption[:60]}"

    def clean(self) -> None:
        if not self.file and not self.external_url:
            raise ValidationError("Add an uploaded file or an external URL.")
        if self.button_label and not self.button_url:
            raise ValidationError("A button label needs a button URL.")


class PageSection(models.Model):
    """A titled block under the slideshow. The screenshot uses Facts & Stats."""

    title = models.CharField(max_length=160)
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return self.title


class Stat(models.Model):
    section = models.ForeignKey(
        PageSection,
        related_name="stats",
        on_delete=models.CASCADE,
    )
    display_value = models.CharField(
        max_length=40,
        help_text='Shown exactly as typed, for example 1,260 or 4TH.',
    )
    description = models.TextField()
    background_color = models.CharField(max_length=20, default="#AD3330")
    text_color = models.CharField(max_length=20, default="#FFFFFF")
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return f"{self.display_value} — {self.section}"
