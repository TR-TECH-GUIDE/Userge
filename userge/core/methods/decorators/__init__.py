# pylint: disable=missing-module-docstring

__all__ = ['Decorators']

from .raw_decorator import RawDecorator  # noqa
from .add_task import AddTask
from .on_cmd import OnCmd
from .on_filters import OnFilters
from .on_left_member import OnLeftMember
from .on_new_member import OnNewMember


class Decorators(AddTask, OnCmd, OnFilters, OnLeftMember, OnNewMember):
    """ methods.decorators """
