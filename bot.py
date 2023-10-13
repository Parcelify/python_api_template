import requests 

from interactions import Client, listen, events 
from config import DISCORD_TOKEN, PARCEL_API_KEY

bot_client = Client(token=DISCORD_TOKEN)

@listen(events.Ready)
async def on_ready():
    print(f"{bot_client.app.name}: Started")
    
    response = requests.get(url="https://v2.parcelroblox.com/hub", 
                            headers={"Authorization": PARCEL_API_KEY}
                            )
    
    if response.json()["status"] == 401:
        return Exception("You have an invalid API KEY. Please regen it via Parcel's dashboard.")    
    
bot_client.start()