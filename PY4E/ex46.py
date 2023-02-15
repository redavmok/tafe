# Davis Burke, 20101583, 11/2/23

total_hours = input("How many hours?")
hour_rate = input("Hourly rate?")
fhr = float(total_hours)
frate = float(hour_rate)


def computepay(hours, rate):
    if fhr > 40:
        ot_hour_total = fhr % 40
        ot_hour_rate = frate * 1.5
        ot_pay_total = ot_hour_total * ot_hour_rate
    else:
        ot_hour_total = 0
        ot_pay_total = 0

    fixed_hours = hours - ot_hour_total
    fixed_pay = fixed_hours * rate
    total_pay = fixed_pay + ot_pay_total
    total_pays = str(total_pay)
    return total_pays


print("Pay " + computepay(fhr, frate))
