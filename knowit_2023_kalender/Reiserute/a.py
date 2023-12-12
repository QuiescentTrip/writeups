with open('knowit_2023_kalender/Reiserute/rute.txt', 'r') as file:
    cities = file.readlines()

start_x, start_y = -1000, -400
total_distance = 0

for city in cities:
    x, y = map(int, city.strip().split(','))
    distance = ((x - start_x)**2 + (y - start_y)**2) ** 0.5
    total_distance += distance
    start_x, start_y = x, y

lyng_lav_behov = (total_distance * 9) / 1000
lyng_lav_behov_avrundet = round(lyng_lav_behov)

print(lyng_lav_behov_avrundet)
