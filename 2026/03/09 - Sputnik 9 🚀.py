def calculate_descent(altitude):
    time = 0

    if altitude > 700:
        time += ((altitude - 700) * 1000) / 2000
        altitude = 700

    if altitude > 85:
        time += ((altitude - 85) * 1000) / 500
        altitude = 85

    if altitude > 50:
        time += ((altitude - 50) * 1000) / 200
        altitude = 50

    if altitude > 12:
        time += ((altitude - 12) * 1000) / 75
        altitude = 12

    if altitude > 0:
        time += (altitude * 1000) / 20

    return round(time, 1)