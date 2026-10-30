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
    footer_heading = models.CharField(max_length=80, default="Connect With Us")
    footer_background_color = models.CharField(max_length=20, default="#C22226")
    footer_text_color = models.CharField(max_length=20, default="#FFFFFF")
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
        help_text="Final label, for example 1,260 or 4TH. The page counts up to it.",
    )
    description = models.TextField()
    count_to = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Number the homepage animates toward. Leave empty to show the label immediately.",
    )
    count_suffix = models.CharField(
        max_length=12,
        blank=True,
        help_text="Appended after the animated number, for example TH.",
    )
    count_duration_ms = models.PositiveIntegerField(default=2000)
    use_grouping = models.BooleanField(
        default=True,
        help_text="Insert thousands separators while the number counts up.",
    )
    background_color = models.CharField(max_length=20, default="#C42127")
    text_color = models.CharField(max_length=20, default="#FFFFFF")
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return f"{self.display_value} — {self.section}"


class LandingBlock(models.Model):
    """A homepage band other than the slideshow and the stat row.

    Promo sits beside the hero media. Feature columns share a group_key and
    one background. News is only the heading for the story list. Impact is
    the closing full-bleed band.
    """

    PROMO = "promo"
    FEATURE = "feature"
    NEWS = "news"
    IMPACT = "impact"
    KIND_CHOICES = [
        (PROMO, "Promo"),
        (FEATURE, "Feature"),
        (NEWS, "News heading"),
        (IMPACT, "Impact"),
    ]

    kind = models.CharField(max_length=16, choices=KIND_CHOICES, default=FEATURE)
    title = models.CharField(max_length=180)
    body = models.TextField(blank=True)
    button_label = models.CharField(max_length=120, blank=True)
    button_url = models.URLField(blank=True, max_length=500)
    image_file = models.ImageField(upload_to="landing/", blank=True)
    image_url = models.URLField(
        blank=True,
        max_length=500,
        help_text="Image URL, or a YouTube link for a promo band.",
    )
    background_color = models.CharField(max_length=20, default="#000000")
    overlay_color = models.CharField(max_length=20, default="#00000099")
    text_color = models.CharField(max_length=20, default="#FFFFFF")
    button_color = models.CharField(max_length=20, default="#FFFFFF")
    button_text_color = models.CharField(max_length=20, default="#C42127")
    group_key = models.CharField(
        max_length=40,
        blank=True,
        help_text="Feature columns with the same key share one background.",
    )
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return f"{self.get_kind_display()}: {self.title}"


class NewsStory(models.Model):
    title = models.CharField(max_length=220)
    url = models.URLField(max_length=500)
    image_file = models.ImageField(upload_to="news/", blank=True)
    image_url = models.URLField(blank=True, max_length=500)
    category = models.CharField(max_length=160, blank=True)
    category_url = models.URLField(blank=True, max_length=500)
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]
        verbose_name_plural = "News stories"

    def __str__(self) -> str:
        return self.title


class FooterOffice(models.Model):
    body = models.TextField(help_text="Line breaks are kept on the page.")
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]
        verbose_name_plural = "Footer offices"

    def __str__(self) -> str:
        return self.body.splitlines()[0][:60]


class SocialLink(models.Model):
    label = models.CharField(max_length=40)
    url = models.URLField()
    position = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["position", "id"]

    def __str__(self) -> str:
        return self.label
