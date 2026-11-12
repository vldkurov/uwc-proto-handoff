from django.apps import AppConfig


class AdminPagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "admin_pages"

    def ready(self):
        import admin_pages.signals  # noqa: F401 (used for side effects)
