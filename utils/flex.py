import logging
from utils.poke_crawler import find_pokemon_name

logger = logging.getLogger(__file__)


def specific_flex(
        image="https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        name=['寶可夢', 'Pokemon'],
        body={'hp': 126, 'attack': 131, 'defense': 95, 'sp_attack': 131, 'sp_defense': 98, 'speed': 99, 'total': 680}):
    logger.debug(f"""
    Specific Pokemon flex generator...
    Image: {image},
    Name list: {name},
    Body status: {body}
    """)
    return {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "horizontal",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "AI",
                                    "size": "sm",
                                    "color": "#ffffff",
                                    "align": "center",
                                    "gravity": "center",
                                    "action": {
                                        "type": "message",
                                        "label": "Image Gen",
                                        "text": f":draw {name[1]}"
                                    }
                                }
                            ],
                            "backgroundColor": "#EC3D44",
                            "paddingAll": "2px",
                            "paddingStart": "4px",
                            "paddingEnd": "4px",
                            "flex": 0,
                            "position": "absolute",
                            "offsetTop": "18px",
                            "width": "48px",
                            "height": "23px",
                            "offsetStart": "18px",
                            "cornerRadius": "100px"
                        }
                    ]
                },
                "hero": {
                    "type": "image",
                    "url": image,
                    "size": "xl",
                    "margin": "none",
                    "aspectMode": "cover",
                    "aspectRatio": "16:16",
                    "action": {
                        "type": "uri",
                        "uri": image
                    }
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": name[0],
                            "color": "#ffffff",
                            "align": "start",
                            "size": "md",
                            "gravity": "center"
                        },
                        {
                            "type": "text",
                            "text": f"HP：{body['hp']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['hp']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                                {
                                                    "type": "filler"
                                                }
                                            ],
                                            "width": f"{body['hp']}%",
                                            "backgroundColor": "#0D8186",
                                            "height": "6px"
                                        }
                                    ],
                                    "backgroundColor": "#9FD8E36E",
                                    "height": "6px",
                                    "margin": "sm"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": f"ATK: {body['attack']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['attack']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": f"DEF：{body['defense']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['defense']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": f"SPA：{body['sp_attack']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['sp_attack']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": f"SPD：{body['sp_defense']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['sp_defense']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },
                        {
                            "type": "text",
                            "text": f"SPE：{body['speed']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "xs",
                            "gravity": "center",
                            "margin": "lg"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                        {
                                            "type": "filler"
                                        }
                                    ],
                                    "width": f"{body['speed']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
                        },                        {
                            "type": "text",
                            "text": f"Total：{body['total']}",
                            "color": "#ffffff",
                            "align": "start",
                            "size": "lg",
                            "gravity": "center",
                            "margin": "lg"
                        }
                    ],
                    "paddingTop": "27px",
                    "paddingAll": "12px",
                    "paddingBottom": "27px",
                    "backgroundColor": "#27ACB2"
                },
                "footer": {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                        {
                            "type": "button",
                            "action": {
                                "type": "message",
                                "label": "Details",
                                "text": f"find {name[1]}"
                            },
                            "style": "primary"
                        }
                    ]
                },
                "styles": {
                    "header": {
                        "separator": False
                    },
                }
            }
        ]
    }


def top_list(name="Pokemon", abilities: list = [[]]):
    contents = [{
        "type": "text",
        "text": name,
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xl"
    }]
    for ability in abilities:
        # TODO: Use Language() to judge language.
        pokemon, _ = find_pokemon_name(ability[0])
        logger.debug(f'ZH-hant name and type are: {pokemon}, {ability[1]}')
        action = {
            "type": "message",
            "label": "action",
            "text": pokemon
        }
        ability[0] = pokemon

        if len(ability) == 2:
            contents.append({
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [{
                        "type": "text",
                        "text": ability[0],
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 5,
                    "action": action
                }, {
                    "type": "text",
                    "text": ability[1],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 5
                }
                ]
            })
        else:
            logger.warning(
                '* Skill list out off range, need to check crawler result.')
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": contents
        }
    }


def skill_list(name="Pokemon", abilities: list = [[]], url: str = 'https://google.com'):
    contents = [{
        "type": "text",
        "text": name,
        "wrap": True,
        "weight": "bold",
        "gravity": "center",
        "size": "xl"
    }]
    for ability in abilities:
        if name == '隊友':
            pokemon, pokemon_type = find_pokemon_name(ability[0])
            logger.debug(
                f'ZH-hant name and type are: {pokemon}, {pokemon_type}')
            action = {
                "type": "message",
                "label": "action",
                "text": pokemon
            }
            ability[0] = pokemon
            ability[1] = pokemon_type if pokemon_type is not None else ability[1]
        else:
            if name != '努力值':
                from urllib import parse
                url = f'https://wiki.52poke.com/wiki/{parse.quote(ability[0].encode("utf-8"))}'
            action = {
                "type": "uri",
                "label": "action",
                "uri": url
            }

        if len(ability) == 2:
            contents.append({
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [{
                        "type": "text",
                        "text": ability[0],
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 5,
                    "action": action
                }, {
                    "type": "text",
                    "text": ability[1],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 5
                }
                ]
            })
        elif len(ability) == 3:
            contents.append({
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [{
                        "type": "text",
                        "text": ability[0],
                        "color": "#aaaaaa",
                        "size": "sm",
                        "flex": 3,
                        "wrap": True,
                    "action": action
                }, {
                    "type": "text",
                    "text": ability[1],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 6
                }, {
                    "type": "text",
                    "text": ability[2],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 3
                }]
            })
        else:
            logger.warning(
                '* Skill list out off range, need to check crawler result.')
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": contents
        }
    }


def replay_flex(sd_user_record, sd_user_record_length):
    # [{"uploadtime":1682434022,"id":"gen9vgc2023regulationc-1851299369","format":"gen9vgc2023regulationc","p1":"picleopa","p2":"Nijiatw"}...]
    two_layer_bubble = {}
    one_layer_content, two_layer_content = [], []
    for idx in range(sd_user_record_length):
        if idx >= 0 and idx < 5:
            one_layer_content.append({
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "replay",
                    "uri": f"https://replay.pokemonshowdown.com/{sd_user_record[idx]['id']}"
                }
            })
        elif idx < 10:
            two_layer_content.append({
                "type": "button",
                "style": "primary",
                "height": "sm",
                "action": {
                    "type": "uri",
                    "label": "replay",
                    "uri": f"https://replay.pokemonshowdown.com/{sd_user_record[idx]['id']}"
                }
            })

            two_layer_bubble = {
                "type": "bubble",
                "hero": {
                        "type": "image",
                        "url": "https://play.pokemonshowdown.com/sprites/gen5/greninja-ash.png",
                        "size": "xl",
                        "aspectMode": "cover",
                        "action": {
                            "type": "uri",
                            "uri": "https://github.com/louis70109/find-your-pokemon"
                        }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": two_layer_content,
                    "flex": 0
                }
            }

    contents = [{
                "type": "bubble",
                "hero": {
                    "type": "image",
                    "url": "https://play.pokemonshowdown.com/sprites/gen5/greninja-ash.png",
                    "size": "xl",
                    "aspectMode": "cover",
                    "action": {
                        "type": "uri",
                        "uri": "https://github.com/louis70109/find-your-pokemon"
                    }
                },
                "footer": {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": one_layer_content,
                    "flex": 0
                }
                }]
    if len(two_layer_bubble) != 0:
        contents.append(two_layer_bubble)
    logger.debug(f"Showdown Carousel content: {contents}")
    return contents
