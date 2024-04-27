from surrealdb import Surreal
import json 

async def main():
    with open('config/surrealdb.json') as f:
        surreal_config = json.load(f)
    username = surreal_config['username']
    password = surreal_config['password']
    databasename = surreal_config["databasename"]
    namespace = surreal_config["namespace"]

    """Example of how to use the SurrealDB client."""
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": username, "pass": password})
        await db.use(namespace, databasename)
        await db.create(
            "person",
            {
                "user": "me",
                "pass": "safe",
                "marketing": True,
                "tags": ["python", "documentation"],
            },
        )
        print(await db.select("person"))
        print(await db.update("person", {
            "user":"you",
            "pass":"very_safe",
            "marketing": False,
            "tags": ["Awesome"]
        }))
        print(await db.delete("person"))

        # You can also use the query method 
        # doing all of the above and more in SurrealQl
        
        # In SurrealQL you can do a direct insert 
        # and the table will be created if it doesn't exist
        await db.query("""
        insert into person {
            user: 'me',
            pass: 'very_safe',
            tags: ['python', 'documentation']
        };
        
        """)
        print(await db.query("select * from person"))
        
        print(await db.query("""
        update person content {
            user: 'you',
            pass: 'more_safe',
            tags: ['awesome']
        };
        
        """))
        print(await db.query("delete person"))

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
