from interactions import Extension, Client  

class WhitelistCog(Extension):
    def __init__(self, client: Client):
        self.client: Client = client
        
def setup(client):
    WhitelistCog(client)