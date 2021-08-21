# pylint: disable=missing-module-docstring

__all__ = ['AddTask']

from typing import Callable, Any

from . import RawDecorator


class AddTask(RawDecorator):  # pylint: disable=missing-class-docstring
    def add_task(self, func: Callable[[], Any]) -> Callable[[], Any]:
        """ add tasks """
        self._tasks.append(func)
        return func
