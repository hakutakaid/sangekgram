#  Pyrofork - Telegram MTProto API Client Library for Python
#  Copyright (C) 2022-present Mayuri-Chan <https://github.com/Mayuri-Chan>
#
#  This file is part of Pyrofork.
#
#  Pyrofork is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrofork is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrofork.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import raw
from ..object import Object


class ForumTopicCreated(Object):
    """A service message about a new forum topic created in the chat.


    Parameters:
        id (``int``):
            Id of the topic

        title (``str``):
            Name of the topic.

        icon_color (``int``):
            Color of the topic icon in decimal format.

        custom_emoji_id (``int``, *optional*):
            Unique identifier of the custom emoji shown as the topic icon.
    """

    def __init__(
        self, *,
        id: int,
        title: str,
        icon_color: int,
        custom_emoji_id: int = None
    ):
        super().__init__()

        self.id = id
        self.title = title
        self.icon_color = icon_color
        self.custom_emoji_id = custom_emoji_id

    @staticmethod
    def _parse(message: "raw.base.Message") -> "ForumTopicCreated":


        return ForumTopicCreated(
            id=getattr(message, "id", None),
            title=getattr(message.action,"title", None),
            icon_color=getattr(message.action,"icon_color", None),
            custom_emoji_id=getattr(message.action,"icon_emoji_id", None)
        )
