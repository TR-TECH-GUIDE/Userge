# pylint: disable=missing-module-docstring

__all__ = ['Methods']

from .chats import Chats
from .decorators import Decorators
from .messages import Messages
from .users import Users
from .utils import Utils


class Methods(Chats, Decorators, Messages, Users, Utils):
    """ userge.methods """
