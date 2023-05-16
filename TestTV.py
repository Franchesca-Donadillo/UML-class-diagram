# Franchesca Marie U. Donadillo
# BSCPE 1-5

from ClassTV import TV

# importing the class TV
tv_1 = TV(channel_tv = int(), volume_level_tv= int(), on_tv= int())

# call channel
tv_1.set_channel(channel_get = int())

# call volume
tv_1.set_volume(volume_level_get = int())

tv_1_1 = TV(channel_tv= 30, volume_level_tv= 3, on_tv= "on")
tv_1_2 = TV(channel_tv= 3, volume_level_tv= 2, on_tv= "on")

print(f"tv_1's channel is {tv_1_1.channel} and volume level is {tv_1_1.volume_level}")
print(f"tv_2's channel is {tv_1_2.channel} and volume level is {tv_1_2.volume_level}")







