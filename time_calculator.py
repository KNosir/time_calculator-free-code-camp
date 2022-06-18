
def add_time(start_time, limit_time, week_day='0'):
    """
    first convert string to list 
    Start_time and limit_time 
    0 index hour
    1 index minute
    2 index AM or PM
    """

    def start_time_string_to_time(input):
        split_input = input.split(' ')
        split_input[0] = split_input[0].split(':')
        first_item = split_input.pop(0)
        split_input.insert(0, int(first_item[0]))
        split_input.insert(1, int(first_item[1]))
        return split_input

    start_time = start_time_string_to_time(start_time)

    limit_time = start_time_string_to_time(limit_time)
    limit_time_minute = limit_time[0]*60 + limit_time[1]

    # finding AM or PM
    am_pm = start_time[2]

    if am_pm == 'AM':
        hour = start_time[0]
        minute = start_time[1]
        if hour == 12:
            hour = 0
            result = minute + limit_time_minute
        else:
            result = hour * 60 + minute + limit_time_minute
    else:
        hour = start_time[0]
        minute = start_time[1]
        if hour != 12:
            hour = hour + 12
            result = hour * 60 + minute + limit_time_minute
        else:
            result = hour * 60 + minute + limit_time_minute
    # end of AM or PM
    # How many days and week_day
    day_number = (result // 60) // 24

    if week_day == '0':
        week_day_print = ''
    elif week_day.lower() == 'monday':
        week_day_print = (1 + day_number) % 8
    elif week_day.lower() == 'tuesday':
        week_day_print = (2 + day_number) % 8
    elif week_day.lower() == 'wednesday':
        week_day_print = (3 + day_number) % 8
    elif week_day.lower() == 'thursday':
        week_day_print = (4 + day_number) % 8
    elif week_day.lower() == 'friday':
        week_day_print = (5 + day_number) % 8
    elif week_day.lower() == 'saturday':
        week_day_print = (6 + day_number) % 8
    elif week_day.lower() == 'sunday':
        week_day_print = (7 + day_number) % 8

    if week_day_print == 1:
        week_day_print = (f', Monday')
    elif week_day_print == 2:
        week_day_print = (f', Tuesday')
    elif week_day_print == 3:
        week_day_print = (f', Wednesday')
    elif week_day_print == 4:
        week_day_print = (f', Thursday')
    elif week_day_print == 5:
        week_day_print = (f', Friday')
    elif week_day_print == 6:
        week_day_print = (f', Saturday')
    elif week_day_print == 7:
        week_day_print = (f', Sunday')

    if day_number == 1:
        day_print = '(next day)'
    elif day_number > 0:
        day_print = f'({day_number} days later)'
    else:
        day_print = ''
    # end of how many days
    # am pm in result
    hour = (result // 60) % 24
    if hour == 0:
        hour = 12
        am_pm = 'AM'
    elif hour > 0 and hour < 11:
        am_pm = 'AM'
    elif hour == 12:
        am_pm = 'PM'
    else:
        hour = hour - 12
        am_pm = 'PM'
    # end of am pm in result

    minute = result % 60
    print(
        f'# Returns: {hour}:{str(minute).zfill(2)} {am_pm}{week_day_print} {day_print}')
#new line