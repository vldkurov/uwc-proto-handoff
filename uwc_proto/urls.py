"""
URL configuration for an uwc_proto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import set_language
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from admin_pages.views import custom_permission_denied_view
from uwc_proto import settings

handler403 = custom_permission_denied_view


urlpatterns = i18n_patterns(
    # Django admin_p
    path(f"{settings.DJANGO_ADMIN_PATH}/", admin.site.urls),
    # Utils
    path("rosetta/", include("rosetta.urls")),
    path("set_language/", set_language, name="set_language"),
    # User management
    path("accounts/", include("allauth.urls")),
    # Public routes
    path("", include("public_pages.urls")),
    path("payments/", include("payments.urls")),
    # Admin routes
    path("dashboard/pages/", include("admin_pages.urls")),
    path("dashboard/locations/", include("locations.urls")),
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
