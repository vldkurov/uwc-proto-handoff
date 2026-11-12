from django.urls import path, re_path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # path("", views.HomePageView.as_view(), name="home"),
    # path("<slug:slug>/", views.GenericPageView.as_view(), name="page"),
    path("", views.GenericPageView.as_view(), {"slug": "home"}, name="home"),
    path("help-and-advice/", RedirectView.as_view(pattern_name="page", permanent=True), {"slug": "ukrainian-heritage"}),
    path("sponsors-hosts/", RedirectView.as_view(pattern_name="page", permanent=True), {"slug": "sponsor-a-refugee"}),
    path("our-distinguished-guests/", RedirectView.as_view(pattern_name="page", permanent=True), {"slug": "our-impact"}),
    re_path(
        r"^(?!public-search)(?P<slug>[\w-]+)/$",
        views.GenericPageView.as_view(),
        name="page",
    ),
    path(
        "locations/redirect",
        views.RedirectToFirstDivisionView.as_view(),
        name="locations_redirect",
    ),
    path("locations/<slug:slug>/", views.LocationsPageView.as_view(), name="locations"),
    path("public-search/", views.public_search, name="public_search"),
]
