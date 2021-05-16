duration = int(input("Введите целочисленное значение в секундах: "))

sec = str(duration)
min = (duration//60)
hour = (duration//3600)
day = (duration//86400)

if duration < 60:
    "секнды"
    print(sec," сек.")
elif duration < 3600:
    "минуты"
    print(min,'мин ', (duration % 60), "секунд")
elif duration < 86400:
    "часы"
    min_x = ((duration % 3600)//60)
    sec_x = (duration - ((hour * 3600) + (min_x * 60)))
    print(str(hour), "часов", min_x, "минут ", sec_x, "секунд ")
else:
    hour_x = ((duration % 86400)//3600)
    min_x = ((duration - ((day * 86400) + (hour_x * 3600)))//60)
    sec_x = ((duration - ((day * 86400) + (hour_x * 3600)))%60)
    print(day, "дней ", hour_x, "часов", min_x, "минут", sec_x, "секунд" )
