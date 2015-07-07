# -*- coding: utf-8 -*-
from pkgutil import get_data

from yaml import load as load_yaml

"""
:mod:`dateparser`'s parsing behavior can be configured like below

*``PREFER_DAY_OF_MONTH``* defaults to ``current`` and can have ``first`` and ``last`` as values::

    >>> from dateparser.conf import settings
    >>> from dateparser import parse
    >>> parse(u'December 2015')
    datetime.datetime(2015, 12, 16, 0, 0)
    >>> settings.update('PREFER_DAY_OF_MONTH', 'last')
    >>> parse(u'December 2015')
    datetime.datetime(2015, 12, 31, 0, 0)
    >>> settings.update('PREFER_DAY_OF_MONTH', 'first')
    >>> parse(u'December 2015')
    datetime.datetime(2015, 12, 1, 0, 0)

*``PREFER_DATES_FROM``* defaults to ``current_period`` and can have ``past`` and ``future`` as values.
Assuming current date is June 16, 2015::

    >>> from dateparser.conf import settings
    >>> from dateparser import parse
    >>> parse(u'March')
    datetime.datetime(2015, 3, 16, 0, 0)
    >>> settings.update('PREFER_DATES_FROM', 'future')
    >>> parse(u'March')
    datetime.datetime(2016, 3, 16, 0, 0)
"""


class Settings(object):
    def __init__(self, **kwargs):
        """
        Settings are now loaded using the data/settings.yaml file.
        """

        data = get_data('data', 'settings.yaml')
        data = load_yaml(data)
        settings_data = data.pop('settings', {})

        for datum in settings_data:
            setattr(self, datum, settings_data[datum])

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def update(self, key, value):
        setattr(self, key, value)


def reload_settings():
    global settings
    settings = Settings()

settings = Settings()
