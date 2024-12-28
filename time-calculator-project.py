def add_time(start_time,duration,starting_day=None):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse start_time
    time, period = start_time.split()
    start_hours, start_minutes = map(int,time.split(':'))
    duration_hours, duration_minutes = map(int,duration.split(':'))

    # Converts the 12-hour format to 24-hour format 
    if period == 'PM' and start_hours != 12:
        start_hours +=12
    elif period == 'AM' and start_hours == 12:
        start_hours = 0
    
    # Add the duration
    total_minutes = start_minutes + duration_minutes
    extra_hours = total_minutes // 60
    final_minutes = total_minutes % 60

    total_hours = start_hours + duration_hours + extra_hours
    days_elapsed = total_hours // 24
    final_hours = total_hours % 24

    # Convert back to 12-hour format
    if final_hours == 0:
        display_hour = 12
        display_period = 'AM'
    elif final_hours < 12:
        display_hour = final_hours
        display_period = 'AM'
    elif final_hours == 12:
        display_hour = 12
        display_period = 'PM'
    else:
        display_hour = final_hours - 12
        display_period = 'PM'
    
    # Handle the day of the week
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        final_day_index = (starting_day_index + days_elapsed) % 7
        final_day = days_of_week[final_day_index]
    else:
        final_day = None

    # Format the result
    result = f"{display_hour}:{final_minutes:02d} {display_period}"
    if final_day:
        result += f", {final_day}"
    if days_elapsed == 1:
        result += " (next day)"
    elif days_elapsed > 1:
        result += f" ({days_elapsed} days later)"

    return result




if __name__== '__main__':
    result = add_time("3:30 PM",'100:12','wednesday')
    print(result)