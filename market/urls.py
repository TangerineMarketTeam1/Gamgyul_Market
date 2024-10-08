from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("products/", views.ProductListView.as_view(), name="product-list"),
    path("products/create/", views.ProductCreateView.as_view(), name="product-create"),
    path(
        "products/<int:id>/", views.ProductDetailView.as_view(), name="product-detail"
    ),
    path(
        "products/<int:id>/update/",
        views.ProductUpdateView.as_view(),
        name="product-update",
    ),
    path(
        "products/<int:id>/delete/",
        views.ProductDeleteView.as_view(),
        name="product-delete",
    ),
    path(
        "products/<int:product_id>/reviews/<int:id>/delete/",
        views.ReviewDeleteView.as_view(),
        name="review-delete",
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
