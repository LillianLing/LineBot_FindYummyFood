from fsm import TocMachine

def create_mechine():
    machine = TocMachine(
        states=["user", "main_menu", "weather_menu", "weather_location", "w_song", "pray_rain", "weather_final", "temp", "sunny", "cloudy", "rainy", "predict_menu", "star_menu", "blood_menu", "divination_menu", "star", "star_property", "star_img", "star_predict", "blood", "blood_property", "tarot", "leave"],
        transitions=[
        {
            "trigger": "advance","source": "user","dest": "main_menu","conditions": "is_going_to_main_menu",
        },{
            "trigger": "advance","source": "main_menu","dest": "weather_menu","conditions": "is_going_to_weather_menu",
        },{
            "trigger": "advance","source": "weather_menu","dest": "weather_location","conditions": "is_going_to_weather_location",
        },{
            "trigger": "advance","source": "weather_location","dest": "weather_final","conditions": "is_going_to_weather_final",
        },{
            "trigger": "advance","source": "weather_final","dest": "temp","conditions": "is_going_to_temp",
        },{
            "trigger": "advance","source": "weather_final","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "weather_location","dest": "temp","conditions": "is_going_to_temp",
        },{
            "trigger": "advance","source": "temp","dest": "weather_final","conditions": "is_going_to_weather_final",
        },{
            "trigger": "advance","source": "temp","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "weather_location","dest": "w_song","conditions": "is_going_to_w_song",
        },{
            "trigger": "advance","source": "w_song","dest": "sunny","conditions": "is_going_to_sunny",
        },{
            "trigger": "advance","source": "sunny","dest": "w_song","conditions": "is_going_to_w_song",
        },{
            "trigger": "advance","source": "w_song","dest": "cloudy","conditions": "is_going_to_cloudy",
        },{
            "trigger": "advance","source": "cloudy","dest": "w_song","conditions": "is_going_to_w_song",
        },{
            "trigger": "advance","source": "w_song","dest": "rainy","conditions": "is_going_to_rainy",
        },{
            "trigger": "advance","source": "rainy","dest": "w_song","conditions": "is_going_to_w_song",
        },{
            "trigger": "advance","source": "w_song","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "weather_location","dest": "pray_rain","conditions": "is_going_to_pray_rain",
        },{
            "trigger": "advance","source": "pray_rain","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "weather_location","dest": "main_menu","conditions": "is_going_to_main_menu",
        },{
            "trigger": "advance","source": "main_menu","dest": "predict_menu","conditions": "is_going_to_predict_menu",
        },{
            "trigger": "advance","source": "predict_menu","dest": "star_menu","conditions": "is_going_to_star_menu",
        },{
            "trigger": "advance","source": "star_menu","dest": "star","conditions": "is_going_to_star",
        },{
            "trigger": "advance","source": "star","dest": "star_property","conditions": "is_going_to_star_property",
        },{
            "trigger": "advance","source": "star_property","dest": "star_img","conditions": "is_going_to_star_img",
        },{
            "trigger": "advance","source": "star_property","dest": "star_predict","conditions": "is_going_to_star_predict",
        },{
            "trigger": "advance","source": "star_property","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "star","dest": "star_img","conditions": "is_going_to_star_img",
        },{
            "trigger": "advance","source": "star_img","dest": "star_property","conditions": "is_going_to_star_property",
        },{
            "trigger": "advance","source": "star_img","dest": "star_predict","conditions": "is_going_to_star_predict",
        },{
            "trigger": "advance","source": "star_img","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "star","dest": "star_predict","conditions": "is_going_to_star_predict",
        },{
            "trigger": "advance","source": "star_predict","dest": "star_property","conditions": "is_going_to_star_property",
        },{
            "trigger": "advance","source": "star_predict","dest": "star_img","conditions": "is_going_to_star_img",
        },{
            "trigger": "advance","source": "star_predict","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "predict_menu","dest": "blood_menu","conditions": "is_going_to_blood_menu",
        },{
            "trigger": "advance","source": "blood_menu","dest": "blood","conditions": "is_going_to_blood",
        },{
            "trigger": "advance","source": "blood","dest": "blood_property","conditions": "is_going_to_blood_property",
        },{
            "trigger": "advance","source": "blood_property","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "predict_menu","dest": "divination_menu","conditions": "is_going_to_divination_menu",
        },{
            "trigger": "advance","source": "divination_menu","dest": "tarot","conditions": "is_going_to_tarot",
        },{
            "trigger": "advance","source": "tarot","dest": "leave","conditions": "is_going_to_leave",
        },{
            "trigger": "advance","source": "predict_menu","dest": "main_menu","conditions": "is_going_to_main_menu",
        },
        { "trigger": "go_back", "source": ["main_menu", "weather_menu","w_song", "pray_rain", "predict_menu", "star", "blood", "leave"], "dest": "user"},
        ],
        initial="user",
        auto_transitions=False,
        show_conditions=True,
    )

    return machine