from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="index"),
    # path("test/", views.test, name="test"),
    # path("details/", views.detail, name="detail"),
    path("video_feed/",views.video_feed, name="video_feed"),
    path("stream/", views.stream, name="stream"),
    path("detail/", views.detail, name="detail"),
    path("offwindow/", views.offwindow, name="offwindow"),
    path("uploadimage/", views.uploadimage, name="uploadimage"),
    path("my_view/",views.my_view, name="my_view"),

]