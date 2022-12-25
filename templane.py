def handle_main_menu():
    return{
        "type": "carousel",
        "contents": [
            {
              "type": "bubble",
              "hero": {
                "type": "image",
                "url": "https://i.imgur.com/S9Izym2.jpg",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                  "type": "uri",
                  "uri": "https://linecorp.com"
                }
              },
              "body": {
                "type": "box",
                "layout": "vertical",
                "spacing": "md",
                "action": {
                  "type": "uri",
                  "uri": "https://linecorp.com"
                },
                "contents": [
                  {
                    "type": "text",
                    "text": "占卜小助手",
                    "size": "xxl",
                    "weight": "bold"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "spacing": "sm",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                          {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_regular_32.png"
                          },
                          {
                            "type": "text",
                            "text": "天氣預報",
                            "weight": "regular",
                            "margin": "sm",
                            "flex": 0
                          },
                          {
                            "type": "text",
                            "text": "明日",
                            "size": "xs",
                            "align": "end",
                            "color": "#aaaaaa"
                          }
                        ]
                      },
                      {
                        "type": "box",
                        "layout": "baseline",
                        "contents": [
                          {
                            "type": "icon",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/restaurant_large_32.png"
                          },
                          {
                            "type": "text",
                            "text": "運勢占卜",
                            "weight": "regular",
                            "margin": "sm",
                            "flex": 0
                          },
                          {
                            "type": "text",
                            "text": "今日",
                            "size": "xs",
                            "align": "end",
                            "color": "#aaaaaa"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "text",
                    "text": "看看今日的運勢及預測明日的天氣!",
                    "wrap": True,
                    "color": "#aaaaaa",
                    "size": "xxs"
                  }
                ]
              },
              "footer": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "button",
                    "margin": "xs",
                    "action": {
                      "type": "message",
                      "label": "天氣預報",
                      "text": "天氣預報"
                    },
                    "height": "sm"
                  },
                  {
                    "type": "button",
                    "action": {
                      "type": "message",
                      "label": "運勢占卜",
                      "text": "運勢占卜"
                    },
                    "margin": "xs",
                    "height": "sm"
                  }
                ],
                "backgroundColor": "#FAEBD7",
                "spacing": "sm"
              },
              "styles": {
                "footer": {
                  "separator": True
                }
              }
            }
        ]
    }

def handle_weather_menu():
    return{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/QG4AgLZ.jpg",
        "size": "full",
        "aspectRatio": "20:15",
        "aspectMode": "cover",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "往後12小時內的天氣",
            "size": "lg",
            "margin": "none",
            "align": "start",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "天氣、降雨機率、濕度",
            "margin": "sm"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "天氣如何",
              "text": "天氣如何"
            }
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/dDRxg7K.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:15",
        "backgroundColor": "#FFFFFF"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "今日氣溫範圍(攝氏)",
            "margin": "none",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "最低溫~最高溫",
            "margin": "sm",
            "size": "md"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "氣溫如何",
              "text": "氣溫如何"
            }
          }
        ]
      },
      "styles": {
        "hero": {
          "separator": True
        },
        "body": {
          "separator": True,
          "backgroundColor": "#87CEFA"
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/KGOYFzL.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "20:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "關於天氣的歌",
            "weight": "bold",
            "margin": "none",
            "size": "md"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "要聽什麼歌呢?",
              "text": "要聽什麼歌呢?"
            },
            "height": "md",
            "margin": "none"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "body": {
          "separator": False
        },
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/izegy6n.jpg",
        "aspectRatio": "20:15",
        "aspectMode": "cover",
        "size": "full"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "求雨儀式",
            "size": "lg",
            "weight": "bold"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "求雨儀式",
              "text": "求雨儀式"
            }
          }
        ]
      },
      "styles": {
        "body": {
          "separator": True
        },
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_song_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/vh6qodE.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "歌單",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "晴天、陰天、雨天各一首",
            "size": "xs",
            "align": "center"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "晴天",
              "text": "晴天"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "陰天",
              "text": "陰天"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "雨天",
              "text": "雨天"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "backgroundColor": "#FAEBD7",
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_sunny_menu():
    return{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Wh3fvxq.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "周杰倫--晴天",
            "weight": "bold"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回",
              "text": "要聽什麼歌呢?"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "alignItems": "flex-start"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "現在馬上聽",
              "uri": "https://www.youtube.com/watch?v=DYptgVvkVLQ"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "backgroundColor": "#FAEBD7",
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_cloudy_menu():
    return{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/4kYJMQR.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "莫文蔚 Karen Mok -- 陰天",
            "weight": "bold"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回",
              "text": "要聽什麼歌呢?"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "alignItems": "flex-start"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "現在馬上聽",
              "uri": "https://www.youtube.com/watch?v=tYWufUugeUc"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "backgroundColor": "#FAEBD7",
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_rainy_menu():
    return{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/I7EyDHr.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "孫燕姿 Sun Yan-Zi -- 雨天",
            "weight": "bold"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回",
              "text": "要聽什麼歌呢?"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "alignItems": "flex-start"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "現在馬上聽",
              "uri": "https://www.youtube.com/watch?v=_zMR-JJMIIE"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "backgroundColor": "#FAEBD7",
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_pray_menu():
    return{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/CgUEMB8.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:15"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "祈雨儀式",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回",
              "text": "返回"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "alignItems": "flex-start"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "前往網站查詢",
              "uri": "https://zh.m.wikipedia.org/zh-tw/%E7%A5%88%E9%9B%A8%E8%88%9E"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "backgroundColor": "#FAEBD7",
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_predict_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/l7brG9Z.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "星座",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "每個星座的特性、圖片和今日運勢",
            "size": "xs"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "前往觀測",
              "text": "星座"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回主選單",
              "text": "主選單"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/OVNfZvE.jpg",
        "size": "full",
        "aspectRatio": "15:13",
        "aspectMode": "cover"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "血型",
            "margin": "none",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "每個血型的性格特徵",
            "size": "xs"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "前往觀測",
              "text": "血型"
            },
            "height": "sm",
            "margin": "none"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回主選單",
              "text": "主選單"
            },
            "margin": "none",
            "height": "sm"
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Wazr9Ho.jpg",
        "aspectRatio": "15:13",
        "aspectMode": "cover",
        "size": "full"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "占卜",
            "margin": "none",
            "size": "lg",
            "weight": "bold"
          },
          {
            "type": "text",
            "text": "各式種類的占卜",
            "size": "xs"
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "前往觀測",
              "text": "占卜"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回主選單",
              "text": "主選單"
            },
            "margin": "none",
            "height": "sm"
          }
        ]
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_star_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/l7brG9Z.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "星座",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "每個星座的特性、圖片和今日運勢",
            "size": "xs"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "特性",
              "text": "特性"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "圖示",
              "text": "圖示"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "今日運勢",
              "text": "今日運勢"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_blood_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/OVNfZvE.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "血型",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "每個血型的性格特徵",
            "size": "xs"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "特性",
              "text": "特性"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_divination_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/Wazr9Ho.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "占卜",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "有名的占卜方式--塔羅牌",
            "size": "xs"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "塔羅牌",
              "text": "塔羅牌"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}

def handle_tarot_menu():
    return {
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/VcTUBlA.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "15:13"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "塔羅牌",
            "weight": "bold",
            "margin": "none",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "介紹與實際占卜",
            "size": "xs"
          }
        ],
        "alignItems": "flex-start",
        "spacing": "none",
        "margin": "none"
      },
      "footer": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "規則介紹",
              "uri": "https://www.youtube.com/watch?v=nZbD9DrmKHE"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "實例(關於愛情)",
              "uri": "https://www.youtube.com/watch?v=-h7R-_6Qs6Y"
            },
            "margin": "none",
            "height": "sm"
          },
          {
            "type": "button",
            "action": {
              "type": "message",
              "label": "返回",
              "text": "返回"
            },
            "margin": "none",
            "height": "sm"
          }
        ],
        "spacing": "none",
        "margin": "none"
      },
      "styles": {
        "footer": {
          "separator": True
        }
      }
    }
  ]
}