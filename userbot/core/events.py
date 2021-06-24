import typing

from telethon import events, functions, hints, types

from ..Config import Config
from .managers import edit_or_reply


@events.common.name_inner_event
class NewMessage(events.NewMessage):
    def __init__(self, require_admin: bool = None, inline: bool = False, **kwargs):
        super().__init__(**kwargs)

        self.require_admin = require_admin
        self.inline = inline

    def filter(self, event):
        _event = super().filter(event)
        if not _event:
            return

        if self.inline is not None and bool(self.inline) != bool(
            event.message.via_bot_id
        ):
            return

        if self.require_admin and not isinstance(event._chat_peer, types.PeerUser):
            is_creator = False
            is_admin = False
            creator = hasattr(event.chat, "creator")
            admin_rights = hasattr(event.chat, "admin_rights")
            if not creator and not admin_rights:
                event.chat = event._client.loop.create_task(event.get_chat())

            if self.incoming:
                try:
                    p = event._client.loop.create_task(
                        event._client(
                            functions.channels.GetParticipantRequest(
                                event.chat_id, event.sender_id
                            )
                        )
                    )
                    participant = p.participant
                except Exception:
                    participant = None
                if isinstance(participant, types.ChannelParticipantCreator):
                    is_creator = True
                if isinstance(participant, types.ChannelParticipantAdmin):
                    is_admin = True
            else:
                is_creator = event.chat.creator
                is_admin = event.chat.admin_rights

            if not is_creator and not is_admin:
                text = "`I need admin rights to be able to use this command!`"

                event._client.loop.create_task(edit_or_reply(event, text))
                return
        return event


@events.common.name_inner_event
class MessageEdited(NewMessage):
    @classmethod
    def build(cls, update, others=None, self_id=None):
        if isinstance(update, types.UpdateEditMessage):
            return cls.Event(update.message)
        if isinstance(update, types.UpdateEditChannelMessage):
            if (
                update.message.edit_date
                and update.message.is_channel
                and not update.message.is_group
            ):
                return
            return cls.Event(update.message)

    class Event(NewMessage.Event):
        pass


async def send_message(
    client,
    entity: "hints.EntityLike",
    message: "hints.MessageLike" = "",
    *,
    reply_to: "typing.Union[int, types.Message]" = None,
    parse_mode: typing.Optional[str] = (),
    formatting_entities: typing.Optional[typing.List[types.TypeMessageEntity]] = None,
    link_preview: bool = True,
    file: "typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]" = None,
    force_document: bool = False,
    clear_draft: bool = False,
    buttons: "hints.MarkupLike" = None,
    silent: bool = None,
    schedule: "hints.DateLike" = None,
    comment_to: "typing.Union[int, types.Message]" = None
):
    chatid = entity
    if str(chatid) == str(Config.BOTLOG_CHATID):
        return await client.sendmessage(
            entity=chatid,
            message=message,
            reply_to=reply_to,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            link_preview=link_preview,
            file=file,
            force_document=force_document,
            clear_draft=clear_draft,
            buttons=buttons,
            silent=silent,
            schedule=schedule,
            comment_to=comment_to,
        )

    msg = message
    if msg and (
        (Config.STRING_SESSION in msg)
        or (str(Config.APP_ID) in msg)
        or (Config.API_HASH in msg)
        or (Config.TG_BOT_TOKEN in msg)
        or (Config.HEROKU_API_KEY and Config.HEROKU_API_KEY in msg)
        or (
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY
            and Config.SCREEN_SHOT_LAYER_ACCESS_KEY in msg
        )
    ):
        if Config.BOTLOG:
            await client.sendmessage(
                entity=Config.BOTLOG_CHATID,
                message=msg,
                reply_to=reply_to,
                parse_mode=parse_mode,
                formatting_entities=formatting_entities,
                link_preview=link_preview,
                file=file,
                force_document=force_document,
                clear_draft=clear_draft,
                buttons=buttons,
                silent=silent,
                schedule=schedule,
                comment_to=comment_to,
            )

        msg = "__Sorry I can't send this information in public chats i will send it in Bot Log group check it from there.__"
        return await client.sendmessage(
            entity=chatid,
            message=msg,
            reply_to=reply_to,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            link_preview=link_preview,
            file=file,
            force_document=force_document,
            clear_draft=clear_draft,
            buttons=buttons,
            silent=silent,
            schedule=schedule,
            comment_to=comment_to,
        )
    return await client.sendmessage(
        entity=chatid,
        message=msg,
        reply_to=reply_to,
        parse_mode=parse_mode,
        formatting_entities=formatting_entities,
        link_preview=link_preview,
        file=file,
        force_document=force_document,
        clear_draft=clear_draft,
        buttons=buttons,
        silent=silent,
        schedule=schedule,
        comment_to=comment_to,
    )


async def send_file(
    client,
    entity: "hints.EntityLike",
    file: "typing.Union[hints.FileLike, typing.Sequence[hints.FileLike]]",
    *,
    caption: typing.Union[str, typing.Sequence[str]] = None,
    force_document: bool = False,
    file_size: int = None,
    clear_draft: bool = False,
    progress_callback: "hints.ProgressCallback" = None,
    reply_to: "hints.MessageIDLike" = None,
    attributes: "typing.Sequence[types.TypeDocumentAttribute]" = None,
    thumb: "hints.FileLike" = None,
    allow_cache: bool = True,
    parse_mode: str = (),
    formatting_entities: typing.Optional[typing.List[types.TypeMessageEntity]] = None,
    voice_note: bool = False,
    video_note: bool = False,
    buttons: "hints.MarkupLike" = None,
    silent: bool = None,
    supports_streaming: bool = False,
    schedule: "hints.DateLike" = None,
    comment_to: "typing.Union[int, types.Message]" = None,
    **kwargs
):
    chatid = entity
    if str(chatid) == str(Config.BOTLOG_CHATID):
        return await client.sendfile(
            entity=chatid,
            file=file,
            caption=caption,
            force_document=force_document,
            file_size=file_size,
            clear_draft=clear_draft,
            progress_callback=progress_callback,
            reply_to=reply_to,
            attributes=attributes,
            thumb=thumb,
            allow_cache=allow_cache,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            voice_note=voice_note,
            video_note=video_note,
            buttons=buttons,
            silent=silent,
            supports_streaming=supports_streaming,
            schedule=schedule,
            comment_to=comment_to,
            **kwargs,
        )

    msg = caption
    if msg and (
        (Config.STRING_SESSION in msg)
        or (str(Config.APP_ID) in msg)
        or (Config.API_HASH in msg)
        or (Config.TG_BOT_TOKEN in msg)
        or (Config.HEROKU_API_KEY and Config.HEROKU_API_KEY in msg)
        or (
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY
            and Config.SCREEN_SHOT_LAYER_ACCESS_KEY in msg
        )
    ):
        if Config.BOTLOG:
            await client.sendfile(
                entity=Config.BOTLOG_CHATID,
                file=file,
                caption=msg,
                force_document=force_document,
                file_size=file_size,
                clear_draft=clear_draft,
                progress_callback=progress_callback,
                reply_to=reply_to,
                attributes=attributes,
                thumb=thumb,
                allow_cache=allow_cache,
                parse_mode=parse_mode,
                formatting_entities=formatting_entities,
                voice_note=voice_note,
                video_note=video_note,
                buttons=buttons,
                silent=silent,
                supports_streaming=supports_streaming,
                schedule=schedule,
                comment_to=comment_to,
                **kwargs,
            )

        msg = "__Sorry I can't send this information in public chats i will send it in Bot Log group check it from there__"
        return await client.sendfile(
            entity=chatid,
            file=file,
            caption=msg,
            force_document=force_document,
            file_size=file_size,
            clear_draft=clear_draft,
            progress_callback=progress_callback,
            reply_to=reply_to,
            attributes=attributes,
            thumb=thumb,
            allow_cache=allow_cache,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            voice_note=voice_note,
            video_note=video_note,
            buttons=buttons,
            silent=silent,
            supports_streaming=supports_streaming,
            schedule=schedule,
            comment_to=comment_to,
            **kwargs,
        )
    return await client.sendfile(
        entity=chatid,
        file=file,
        caption=msg,
        force_document=force_document,
        file_size=file_size,
        clear_draft=clear_draft,
        progress_callback=progress_callback,
        reply_to=reply_to,
        attributes=attributes,
        thumb=thumb,
        allow_cache=allow_cache,
        parse_mode=parse_mode,
        formatting_entities=formatting_entities,
        voice_note=voice_note,
        video_note=video_note,
        buttons=buttons,
        silent=silent,
        supports_streaming=supports_streaming,
        schedule=schedule,
        comment_to=comment_to,
        **kwargs,
    )


async def edit_message(
    client,
    entity: "typing.Union[hints.EntityLike, types.Message]",
    message: "hints.MessageLike" = None,
    text: str = None,
    *,
    parse_mode: str = (),
    formatting_entities: typing.Optional[typing.List[types.TypeMessageEntity]] = None,
    link_preview: bool = True,
    file: "hints.FileLike" = None,
    force_document: bool = False,
    buttons: "hints.MarkupLike" = None,
    schedule: "hints.DateLike" = None
):
    chatid = entity
    if str(chatid) == str(Config.BOTLOG_CHATID):
        return await client.editmessage(
            entity=entity,
            message=message,
            text=text,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            link_preview=link_preview,
            file=file,
            force_document=force_document,
            buttons=buttons,
            schedule=schedule,
        )
    main_msg = text
    if main_msg and (
        (Config.STRING_SESSION in main_msg)
        or (str(Config.APP_ID) in main_msg)
        or (Config.API_HASH in main_msg)
        or (Config.TG_BOT_TOKEN in main_msg)
        or (Config.HEROKU_API_KEY and Config.HEROKU_API_KEY in main_msg)
        or (
            Config.SCREEN_SHOT_LAYER_ACCESS_KEY
            and Config.SCREEN_SHOT_LAYER_ACCESS_KEY in main_msg
        )
    ):
        if Config.BOTLOG:
            await client.sendmessage(
                entity=Config.BOTLOG_CHATID,
                message=main_msg,
                parse_mode=parse_mode,
                formatting_entities=formatting_entities,
                link_preview=link_preview,
                file=file,
                force_document=force_document,
                buttons=buttons,
                schedule=schedule,
            )
        msg = "__Sorry I can't send this information in public chats i will send it in Bot Log group check it from there__"
        return await client.editmessage(
            entity=chatid,
            message=message,
            text=msg,
            parse_mode=parse_mode,
            formatting_entities=formatting_entities,
            link_preview=link_preview,
            file=file,
            force_document=force_document,
            buttons=buttons,
            schedule=schedule,
        )
    return await client.editmessage(
        entity=chatid,
        message=message,
        text=main_msg,
        parse_mode=parse_mode,
        formatting_entities=formatting_entities,
        link_preview=link_preview,
        file=file,
        force_document=force_document,
        buttons=buttons,
        schedule=schedule,
    )
