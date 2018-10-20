from rest_framework import routers, serializers, viewsets
from bot_cms_apiw.models import File, Folder


# Serializers define the API representation.
class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ('belong_to_folder_id', 'title', 'content', 'template_path',
                  'seo_title', 'seo_keywords', 'seo_des', 'gmt_auto_pub',)


# ViewSets define the view behavior.
class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer


class FolderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Folder
        fields = ('parent_folder_id', 'name', 'depth', 'template_path',)


# ViewSets define the view behavior.
class FolderViewSet(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'file', FileViewSet)
router.register(r'folder', FolderViewSet)
