"""
URL configuration for web_django project.
"""
from django.contrib import admin
from django.urls import path, include, re_path

# Import cho MEDIA
from django.conf import settings
from django.views.static import serve

# Danh sách điều hướng các trang trên website
urlpatterns = [
    path('admin/', admin.site.urls), # Đường dẫn vào trang quản trị hệ thống
    path('', include('app.urls', namespace='app')),   # Dẫn các yêu cầu còn lại vào file urls của app
]

# Kích hoạt hiển thị hình ảnh (sản phẩm, avatar...) khi đang chạy ở máy cá nhân
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
