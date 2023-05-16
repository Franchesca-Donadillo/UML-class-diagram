# Franchesca Marie U. Donadillo
# BSCPE 1-5

# importing the class TV
from ClassTV import TV

# initializing parameter
tv = TV(channel_tv = int(), volume_level_tv= int(), on_tv= int())

# create class object
tv_1 = TV(channel_tv= 30, volume_level_tv= 3, on_tv= "on")
tv_2 = TV(channel_tv= 3, volume_level_tv= 2, on_tv= "on")


# calling object 1
print("tv_1's", end = " ")
tv_1.set_channel(1)  
tv_1.set_volume(1)

# calling object 2
print("tv_2's", end = " ")
tv_2.set_channel(1)
tv_2.set_volume(1)

tv_1.channel_up()
tv_1.volume_up()









