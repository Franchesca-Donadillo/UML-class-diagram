# Franchesca Marie U. Donadillo
# BSCPE 1-5

from ClassTV import TV

# importing the class TV
tv_1 = TV(channel_tv = int(), volume_level_tv= int(), on_tv= int())

# call channel
tv_1.get_channel() 
tv_1.set_channel(channel_get = int())

# call volume
tv_1.get_volume()
tv_1.set_volume(volume_level_get = int())

tv_1_1 = TV(channel_tv= int(), volume_level_tv= int(), on_tv= " ")
print(f"tv_1's channel is {tv_1_1.channel}")







