# davis burke, 20101583, 11/2/23

hours = input("How many hours?")
rate = input("Hourly rate?")

# this block converts the input to float point number
hours2 = float(hours)
rate2 = float(rate)

# this block guards against no overtime
if hours2 % 40 > 0:
    ot_hours = hours2 % 40
else:
    ot_hours = 0

# this block calculates how much overtime pay is paid
ot_rate = rate2 * 1.5
ot_pay = ot_hours * ot_rate

# this calculates the hours that are paid at the normal rate
hours3 = hours2 - ot_hours

# this calculates normal pay (normal hours by normal rate)
normal_pay = hours3 * rate2

# final pay
final_rate = ot_pay + normal_pay

print(final_rate)
