from modules.power_level import PowerLevel


serial = 42 # 42 # 18 # 7403
gridsize = 300
 
powerLevel = PowerLevel(serial, gridsize)
#powerLevel.show_max_power_level()  # by window width

#mg = powerLevel.max_grid(window_size=200)
#print(f'{mg}')

x, y, s = powerLevel.optimal_window_size()
print(f'Part 2: {x},{y},{s}')

#print('fin')

