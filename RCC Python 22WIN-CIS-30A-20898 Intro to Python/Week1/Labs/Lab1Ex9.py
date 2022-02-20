#Python program to calculate the total shipping cost for electronics

ship_rate = 2.66
tablet_weight = 1
laptop_weight = 7
TV_weight = 37

ship_tablet = tablet_weight * ship_rate
print('Shipping cost of tablet: $ {:.2f}'.format(ship_tablet))

ship_laptop = laptop_weight * ship_rate
print('Shipping cost of laptop: $ {:.2f}'.format(ship_laptop))

ship_TV = TV_weight * ship_rate
print('Shipping cost of TV: $ {:.2f}'.format(ship_TV))

total_ship = ship_tablet + ship_laptop + ship_TV
print('Shipping cost of 3 devices: $ {:.2f}'.format(total_ship))