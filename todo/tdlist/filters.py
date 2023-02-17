from django_filters import rest_framework as dj_filters
from .models import Tasklist


class TasklistFilterSet(dj_filters.FilterSet):
    """Набор фильров для представления для модели задач"""

    taskText = dj_filters.CharFilter(field_name="taskText", lookup_expr="icontains")
    is_done = dj_filters.BooleanFilter(field_name="is_done")
    order_by_field = "ordering"

    class Meta:
        model = Tasklist
        fields = [
            "taskText",
        ]
