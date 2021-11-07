from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from ninja import NinjaAPI

from medcyclopedia.controllers.articles_controller import articles_controller
from medcyclopedia.controllers.categories_controller import categories_controller
from medcyclopedia.controllers.tags_controller import tags_controller
from medcyclopedia.controllers.drug_controller import drug_controller
from medcyclopedia.controllers.drugClass_controller import drugClass_controller

api = NinjaAPI(
    version='1.0.0',
    title='client API v1',
    description='API documentation',
)

api.add_router('/articles', articles_controller)
api.add_router('/categories', categories_controller)
api.add_router('/tags', tags_controller)
api.add_router('/drug', drug_controller)
api.add_router('/drugClass', drugClass_controller)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls)
]

# if settings.DEBUG:
#     urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
