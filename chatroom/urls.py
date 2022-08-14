from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include

import base


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('base.urls')),
    path('api/', include('base.api.urls'))
]
