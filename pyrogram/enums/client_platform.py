#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from enum import auto

from .auto_name import AutoName


class ClientPlatform(AutoName):
    """Valid platforms for a :obj:`~pyrogram.Client`."""

    ANDROID = auto()
    "Android"

    IOS = auto()
    "iOS"

    WP = auto()
    "Windows Phone"

    BB = auto()
    "Blackberry"

    DESKTOP = auto()
    "Desktop"

    WEB = auto()
    "Web"

    UBP = auto()
    "Ubuntu Phone"

    OTHER = auto()
    "Other"
