from typing import Any, Optional

from django.db.models.expressions import Func
from django.db.models.functions.mixins import FixDurationInputMixin, NumericOutputFieldMixin

class Aggregate(Func):
    filter_template: str = ...
    filter: Any = ...
    allow_distinct: bool = ...
    def __init__(self, *expressions: Any, distinct: bool = ..., filter: Optional[Any] = ..., **extra: Any) -> None: ...

class Avg(FixDurationInputMixin, NumericOutputFieldMixin, Aggregate): ...
class Count(Aggregate): ...
class Max(Aggregate): ...
class Min(Aggregate): ...
class StdDev(NumericOutputFieldMixin, Aggregate): ...
class Sum(FixDurationInputMixin, Aggregate): ...
class Variance(NumericOutputFieldMixin, Aggregate): ...
