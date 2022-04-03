def coverts_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remain_second = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remain_second


(hours, minutes, seconds) = coverts_seconds(1000)
print(hours, minutes, seconds)
