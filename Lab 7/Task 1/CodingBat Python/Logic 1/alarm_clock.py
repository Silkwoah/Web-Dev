def alarm_clock(day, vacation):
    if not vacation:
        if 1 <= day <= 5:
            return '7:00'
        else:
            return '10:00'
    else:
        if 1 <= day <= 5: 
            return '10:00'
        else:
            return 'off'