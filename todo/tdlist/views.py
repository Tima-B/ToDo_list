# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt

from django.views.generic import (
    DetailView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
)
from tdlist.models import Tasklist
from rest_framework import viewsets, mixins
from .serializers import TasklistSerializer
from .filters import TasklistFilterSet
from rest_framework.schemas.openapi import AutoSchema


class TasklistViewSet(
    mixins.ListModelMixin,  # GET /Tasllist
    mixins.CreateModelMixin,  # POST /Tasllist
    mixins.RetrieveModelMixin,  # GET /Tasllist/1
    mixins.DestroyModelMixin,  # DELETE /Tasllist/1
    mixins.UpdateModelMixin,  # PUT /Tasllist/1
    viewsets.GenericViewSet,
):
    queryset = Tasklist.objects.all().order_by("-id")
    serializer_class = TasklistSerializer
    filterset_class = TasklistFilterSet

    schema = AutoSchema(
        tags=["Tasklist"],
        component_name="Tasklist",
        operation_id_base="Tasklist",
    )

    # pagination_class = None
    # permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return NonModelSerializer
    #     return ArticleSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TaskDetailView(DetailView):
    """Представление для отображения одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#detailview
    """

    context_object_name = "task"
    model = Tasklist
    #    queryset = Tasklist.objects.filter(is_done=False)
    template_name = "task_detail.html"


class TaskListView(ListView):
    """Представление для отображения множества корзин.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    context_object_name = "tasks_"
    #   queryset = Tasklist.objects.filter(is_done=False)
    model = Tasklist
    template_name = "task_list.html"


class TaskListViewActive(ListView):

    context_object_name = "tasks_"
    queryset = Tasklist.objects.filter(is_done=False)
    model = Tasklist
    template_name = "task_list.html"


class TaskCreateView(CreateView):
    """Представление для создания одной корзины.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-editing/#django.views.generic.edit.CreateView
    """

    model = Tasklist
    fields = ["taskText", "created_time", "is_done"]
    template_name = "task_create.html"
    success_url = "/tasks/"


class TaskUpdateView(UpdateView):
    model = Tasklist
    fields = ["taskText", "created_time", "is_done"]
    template_name = "task_update.html"
    success_url = "/tasks/"


class TaskDeleteView(DeleteView):
    model = Tasklist
    template_name = "task_delete.html"
    success_url = "/tasks/"
