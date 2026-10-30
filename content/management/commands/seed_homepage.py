import os
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen

from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction

from content.models import (
    ActionLink,
    FooterOffice,
    HeroSlide,
    LandingBlock,
    NavItem,
    NewsStory,
    PageSection,
    SiteSettings,
    SocialLink,
    Stat,
)
from content.seed_data import (
    ACTION_LINKS,
    FACTS_TITLE,
    FOOTER_OFFICES,
    LANDING_BLOCKS,
    NAVIGATION,
    NEWS_STORIES,
    PREDEFINED_EMAIL,
    PREDEFINED_PASSWORD,
    PREDEFINED_USERNAME,
    SITE,
    SLIDES,
    SOCIAL_LINKS,
    STATS,
)


class Command(BaseCommand):
    help = "Replace homepage content with the UGHE screenshot data and reset the staff account."

    def handle(self, *args, **options):
        with transaction.atomic():
            self._clear()
            self._site()
            self._actions()
            self._navigation()
            self._slides()
            self._facts()
            self._landing()
            self._news()
            self._footer()
            self._staff_user()
        self.stdout.write(self.style.SUCCESS("Homepage content is loaded."))
        self.stdout.write(f"Django admin and API username: {PREDEFINED_USERNAME}")
        self.stdout.write(f"Password: {PREDEFINED_PASSWORD}")

    def _clear(self) -> None:
        Stat.objects.all().delete()
        PageSection.objects.all().delete()
        NewsStory.objects.all().delete()
        LandingBlock.objects.all().delete()
        FooterOffice.objects.all().delete()
        SocialLink.objects.all().delete()
        HeroSlide.objects.all().delete()
        ActionLink.objects.all().delete()
        NavItem.objects.all().delete()
        SiteSettings.objects.all().delete()

    def _site(self) -> None:
        settings_row = SiteSettings.objects.create(**SITE)
        logo = self._download(SITE["logo_url"])
        if logo is not None:
            settings_row.logo_file.save(logo.name, logo, save=True)

    def _actions(self) -> None:
        for position, link in enumerate(ACTION_LINKS, start=1):
            ActionLink.objects.create(position=position, open_in_new_tab=True, **link)

    def _navigation(self) -> None:
        for position, item in enumerate(NAVIGATION, start=1):
            parent = NavItem.objects.create(
                label=item["label"],
                url=item["url"],
                position=position,
                open_in_new_tab=bool(item["url"]),
            )
            for child_position, child in enumerate(item["children"], start=1):
                NavItem.objects.create(
                    parent=parent,
                    label=child["label"],
                    url=child["url"],
                    position=child_position,
                    open_in_new_tab=True,
                )

    def _slides(self) -> None:
        for position, slide in enumerate(SLIDES, start=1):
            row = HeroSlide.objects.create(position=position, **slide)
            if row.media_type != HeroSlide.IMAGE:
                continue
            image = self._download(row.external_url)
            if image is not None:
                row.file.save(image.name, image, save=True)

    def _download(self, url: str) -> ContentFile | None:
        """Copy a public UGHE asset into local media so the page does not depend on hotlinking."""
        if os.environ.get("SKIP_MEDIA_DOWNLOAD") == "1":
            return None
        try:
            request = Request(url, headers={"User-Agent": "UGHE-Test-Web-App"})
            with urlopen(request, timeout=40) as response:
                payload = response.read()
        except (URLError, TimeoutError, OSError) as exc:
            self.stderr.write(f"Kept the remote URL for {url} ({exc}).")
            return None
        filename = Path(url.split("?", 1)[0]).name or "asset"
        return ContentFile(payload, name=filename)

    def _facts(self) -> None:
        section = PageSection.objects.create(title=FACTS_TITLE, position=1)
        for position, stat in enumerate(STATS, start=1):
            Stat.objects.create(section=section, position=position, **stat)

    def _save_image(self, row, url: str) -> None:
        if not url or "youtu" in url:
            return
        image = self._download(url)
        if image is not None:
            row.image_file.save(image.name, image, save=True)

    def _landing(self) -> None:
        for position, block in enumerate(LANDING_BLOCKS, start=1):
            row = LandingBlock.objects.create(position=position, **block)
            self._save_image(row, row.image_url)

    def _news(self) -> None:
        for position, story in enumerate(NEWS_STORIES, start=1):
            row = NewsStory.objects.create(position=position, **story)
            self._save_image(row, row.image_url)

    def _footer(self) -> None:
        for position, office in enumerate(FOOTER_OFFICES, start=1):
            FooterOffice.objects.create(position=position, **office)
        for position, link in enumerate(SOCIAL_LINKS, start=1):
            SocialLink.objects.create(position=position, **link)

    def _staff_user(self) -> None:
        User = get_user_model()
        user, _created = User.objects.get_or_create(
            username=PREDEFINED_USERNAME,
            defaults={"email": PREDEFINED_EMAIL},
        )
        user.email = PREDEFINED_EMAIL
        user.is_staff = True
        user.is_superuser = True
        user.set_password(PREDEFINED_PASSWORD)
        user.save()
