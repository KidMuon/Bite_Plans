from surrealdb import Surreal
import json, asyncio

class SurrealDatabase():
    def __init__(self):
        with open('config/surrealdb.json') as f:
            self.config = json.load(f)
        self.username = self.config['username']
        self.password = self.config['password']
        self.database = self.config['databasename']
        self.namespace = self.config['namespace']
        self.port = self.config['port']
        self.connect_string = "ws://localhost:"
        self.connect_string += str(self.port)
        self.connect_string += "/rpc"
        return None
    
    def select(self, table):
        asyncio.run(self._select_surreal(table))

    def create(self, table, data):
        asyncio.run(self._create_surreal(table, data))

    async def _select_surreal(self, table):
        async with Surreal(self.connect_string) as surreal_database:
            await surreal_database.signin(
                {"user": self.username,
                "pass": self.password}
                )
            await surreal_database.use(
                self.namespace, 
                self.database
                )
            print(await surreal_database.select(table))
    
    async def _create_surreal(self, table, data):
        async with Surreal(self.connect_string) as surreal_database:
            await surreal_database.signin(
                {"user": self.username,
                "pass": self.password}
                )
            await surreal_database.use(
                self.namespace, 
                self.database
                )
            surreal_database.create(table, data)