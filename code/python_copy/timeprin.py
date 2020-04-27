import time

named_tuple = time.localtime()
time_string = time.strftime("%H:%M:%S", named_tuple)

print(time_string)

# for i in range(0,12):
#     print(f'Fuck off for the {i}th times')

# end_time = time.time() - start_time
# print(f'End time : {end_time}')