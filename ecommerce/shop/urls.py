from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.ProductListView.as_view(), name='shop'),
    path('product/<str:product_slug>/', views.ProductDetailView.as_view(),
         name='product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
