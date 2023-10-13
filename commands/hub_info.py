from interactions import Extension, Client, slash_command

class HubInfoCog(Extension):
    def __init__(self, client: Client):
        self.client: Client = client
    @slash_command(name="info", description="information about the hub")
    async def hub(self):
        pass 
        
def setup(client):
    HubInfoCog(client)