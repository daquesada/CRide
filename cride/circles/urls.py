from django.urls import path

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),

]