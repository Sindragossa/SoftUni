rests_days = int(input())
work_days = 365 - rests_days
norm = 30000
days_in_year = 365

play_work = work_days * 63
play_rest = rests_days * 127

all_play_time = play_rest + play_work

if all_play_time > norm:
    everything = all_play_time - norm
    print('Tom will run away')
    if everything > 60:
        everything_h = everything // 60
        everything_m = everything - (everything_h * 60)
        print(f'{everything_h} hours and {everything_m} minutes more for play')

else:
    print(f'Tom sleeps well')

    over_the_norm = norm - all_play_time
    if over_the_norm > 60:
        over_the_norm_h = over_the_norm // 60
        over_the_norm_m = over_the_norm - (over_the_norm_h * 60)
        print(f'{over_the_norm_h} hours and {over_the_norm_m} minutes less for play')





