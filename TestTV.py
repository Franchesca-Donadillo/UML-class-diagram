# Franchesca Marie U. Donadillo
# BSCPE 1-5

from ClassTV import TV

television = TV()
television.Start()

while True:
    ask_user = television.AskUser()

    # create tv_1
    tv_1 = TV()
    tv_1.channel = channel
    print(tv_1.channel)