from interactions import Extension, Client  

class ProductsCog(Extension):
    def __init__(self, client: Client):
        self.client: Client = client
        
def setup(client):
    ProductsCog(client)