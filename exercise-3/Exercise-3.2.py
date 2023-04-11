# Calculation to print the time when alarm goes off
current_time = 14

# set the alarm to go off 535 hours later
alarm_hours = 535

# time that alarm will go off
hour_in_day = 24
time = str((current_time + alarm_hours % hour_in_day))

print(time + ".00")

# Ans from source
print(14+535 % 24)
