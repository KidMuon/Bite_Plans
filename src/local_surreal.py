from surrealdb import Surreal
from surrealdb.ws import SurrealPermissionException
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
        return asyncio.run(self._select_surreal(table))

    def create(self, table, data):
        asyncio.run(self._create_surreal(table, data))

    def get_query(self, query):
        return asyncio.run(self._get_query(query))

    def update(self, table, data):
        asyncio.run(self._update_surreal(table, data))

    def get_column_from_table(self, column, table):
        results = []
        if isinstance(column, list):
            query = "SELECT " + ", ".join(column) + " FROM " + table
        else:
            query = "SELECT " + column + " FROM " + table
        raw_result = self.get_query(query)
        #for name in [x[column] for x in raw_result[0]['result']]:
        #    results.append(name)
        return raw_result[0]['result']

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
            records = await surreal_database.select(table)
        return records
    
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
            try:
                await surreal_database.create(table, data)
            except SurrealPermissionException:
                await surreal_database.update(table, data)

    async def _get_query(self, query):
        async with Surreal(self.connect_string) as surreal_database:
            await surreal_database.signin(
                {"user": self.username,
                "pass": self.password}
                )
            await surreal_database.use(
                self.namespace, 
                self.database
                )
            return await surreal_database.query(query)
    
    async def _update_surreal(self, table, data):
        async with Surreal(self.connect_string) as surreal_database:
            await surreal_database.signin(
                {"user": self.username,
                "pass": self.password}
                )
            await surreal_database.use(
                self.namespace, 
                self.database
                )
            await surreal_database.update(table, data)