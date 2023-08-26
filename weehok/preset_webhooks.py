from .weehok import DiscordHook, Embed

def green_embed(title, description, footer, image, thumbnail, author, fields) -> Embed:
    return Embed(title, description, footer, image, thumbnail, author, fields, color=0x00ff00)

def red_embed(title, description, footer, image, thumbnail, author, fields) -> Embed:
    return Embed(title, description, footer, image, thumbnail, author, fields, color=0xff0000)

def blue_embed(title, description, footer, image, thumbnail, author, fields) -> Embed:
    return Embed(title, description, footer, image, thumbnail, author, fields, color=0x0000ff)

def yellow_embed(title, description, footer, image, thumbnail, author, fields) -> Embed:
    return Embed(title, description, footer, image, thumbnail, author, fields, color=0xffff00)


def test_webhook(url: str):
    DiscordHook(url).set_username("test").set_content("test").send()

def send_embed(url: str, embed: Embed):
    DiscordHook(url).add_embed(embed).set_username("<empty>").set_content("<empty>").send()