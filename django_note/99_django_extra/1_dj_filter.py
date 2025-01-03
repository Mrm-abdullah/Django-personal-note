""" 
    today = str(datetime.today().date())
    yesterday = str(datetime.today().date()-timedelta(days=1))
    compleat_ta = Earning_Amount.objects.filter(user=user, level_from='0')
    compleat_task = 0
    for compleat in compleat_ta:
        if str(compleat.created_at.date()) == today:
            compleat_task += 1
"""