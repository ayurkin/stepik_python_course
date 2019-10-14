from datetime import date, timedelta

year, month, day = map(int, input().split())
delta_day = int(input())
print((date(year, month, day) + timedelta(days=delta_day)).strftime("%Y %-m %-d"))
#
# # print(' '.join(str(i) for i in [new_date.year, new_date.month, new_date.day]))
# # print(new_date.year, new_date.month, new_date.day)
# # print(f'{inp.year} {inp.month} {inp.day}')
# # print("{} {} {}".format(current.year, current.month, current.day))


# from datetime import datetime, timedelta
# date_string = input()
# date = int(input())
# ds = datetime.strptime(date_string, '%Y %m %d') + timedelta(days = date)
# print(ds.strftime('%Y %-m %-d'))