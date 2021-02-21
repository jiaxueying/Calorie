"""
user.api
"""


def getCal(user):
    gender = user['gender']
    weight = user['weight']
    height = user['height']
    age = user['age']
    plan = user['plan']
    rate = -float(user['rate'])

    if gender == 'male':
        base_rate = 10*weight+6.25*height-5*age+5
    else:
        base_rate = 10*weight+6.25*height-4.5*age-161

    res = {}

    if plan:
        res['min'] = 1.2*base_rate-7700*rate
        res['max'] = 1.9*base_rate-7700*rate
    else:
        res['min'] = 1.2*base_rate-weight*0.01*1100
        res['max'] = 1.9*base_rate-weight*0.01*1100

    return res
