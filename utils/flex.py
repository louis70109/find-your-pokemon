import urllib.parse
from utils.poke_crawler import find_pokemon_name


def specific_flex(
        image="https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png",
        name="Pokemon",
        body={'hp': 60, 'atk': 45, 'def': 50, 'spa': 90, 'spd': 80, 'spe': 70}):

    return {
        "type": "carousel",
        "contents": [
            {
                "type": "bubble",
                "size": "mega",
                "direction": "ltr",
                "hero": {
                    "type": "image",
                    "url": image,
                    "size": "full",
                    "margin": "none",
                    "aspectMode": "cover",
                    "aspectRatio": "16:16"
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": name,
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
                            "text": f"攻擊: {body['atk']}",
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
                                    "width": f"{body['atk']}%",
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
                            "text": f"防禦：{body['def']}",
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
                                    "width": f"{body['def']}%",
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
                            "text": f"特攻：{body['spa']}",
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
                                    "width": f"{body['spa']}%",
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
                            "text": f"特防：{body['spd']}",
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
                                    "width": f"{body['spd']}%",
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
                            "text": f"速度：{body['spe']}",
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
                                    "width": f"{body['spe']}%",
                                    "backgroundColor": "#0D8186",
                                    "height": "6px"
                                }
                            ],
                            "backgroundColor": "#9FD8E36E",
                            "height": "6px",
                            "margin": "sm"
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
                                "label": "細節",
                                "text": f"find {name}"
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
            action = {
                "type": "message",
                "label": "action",
                "text": pokemon
            }
            ability[0] = pokemon
            ability[1] = pokemon_type if pokemon_type is not None else ability[1]
        else:
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
                        "flex": 4,
                        "wrap": True,
                    "action": action
                }, {
                    "type": "text",
                    "text": ability[1],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 3
                }, {
                    "type": "text",
                    "text": ability[2],
                    "wrap": True,
                    "size": "sm",
                    "color": "#666666",
                    "flex": 3
                }]
            })
    return {
        "type": "bubble",
        "body": {
            "type": "box",
            "layout": "vertical",
            "spacing": "md",
            "contents": contents
        }
    }
