from aiogram import Dispatcher

from loader import dp
from .group_filter import IsGroup, IsGroupCall
from .admins import AdminFilter
from .private_filter import IsPrivate, IsPrivates


if __name__ == "filters":
    dp.filters_factory.bind(IsGroup)
    dp.filters_factory.bind(IsGroupCall)
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsPrivates)
