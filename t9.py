def convert_s_to_format(sec):
    days = sec // (24 * 60 * 60)
    h = (sec - days * 24 * 60 * 60) // (60 * 60)
    m = (sec - days * 24 * 60 * 60 - h * 60 * 60) // 60
    sec1 = sec - (days * 24 * 60 * 60 + h * 60 * 60 + m * 60)
    print(f'{days}:{h}:{m}:{sec1}')


convert_s_to_format(1234565)


def convert(seconds):
    days = seconds // (24 * 3600)
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print(f'{days}:{hours}:{minutes}:{seconds}')


convert(1234565)
