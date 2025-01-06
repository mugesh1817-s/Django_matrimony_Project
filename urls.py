from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('read/',views.read, name='read'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('edit/<int:id>/update/',views.update, name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('successstory/',views.successstory,name='successstory'),
    path('successstory/createnew/',views.createnew,name='createnew'),
    path('storyedit/<int:id>/',views.storyedit,name='storyedit'),
    path('remove/<int:id>/',views.remove, name='remove'),
    path('adminstory/',views.adminstory,name='adminstory'),
    path('expense/',views.adminexpense,name='adminexpense'),
    path('createexp/',views.createexp,name='createexp'),
    path('displayexp/',views.displayexp,name='displayexp'),
    path('deleteexp/<int:id>/',views.deleteexp, name='deleteexp'),
    # path('membercount/',views.membercount,name='membercount'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)