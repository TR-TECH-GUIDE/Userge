# pylint: disable=missing-module-docstring

from userge.logger import logging  # noqa
from userge.config import Config, get_version  # noqa
from userge.core import (  # noqa
    Userge, filters, Message, get_collection, pool)

userge = Userge()  # userge is the client name
