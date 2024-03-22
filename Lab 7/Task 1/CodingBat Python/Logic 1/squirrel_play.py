def squirrel_play(temperature, is_summer):
    if is_summer:
        return 60 <= temperature <= 100
    else:
        return 60 <= temperature <= 90