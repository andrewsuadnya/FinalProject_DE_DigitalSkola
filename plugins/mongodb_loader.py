import pymongo


def get_mongo_client(mongo_uri):
    """Establish connection to the MongoDB."""
    try:
        client = pymongo.MongoClient(mongo_uri)
        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")

            return client
        except Exception as e:
            print(e)
    except pymongo.errors.ConnectionFailure as e:
        print(f"Connection failed: {e}")
        return None


def load(database, collection):
    mongo_uri = "mongodb+srv://temp_user:temp_user123@learn-mongo.hqbsm9p.mongodb.net/?retryWrites=true&w=majority&appName=learn-mongo"
    if not mongo_uri:
        print("MONGO_URI not set in environment variables")

    mongo_client = get_mongo_client(mongo_uri)

    # Ingest data into MongoDB
    db = mongo_client[database]
    col = db[collection]

    return col


def get(database, collection):
    mongo_uri = "mongodb+srv://temp_user:temp_user123@learn-mongo.hqbsm9p.mongodb.net/?retryWrites=true&w=majority&appName=learn-mongo"
    if not mongo_uri:
        print("MONGO_URI not set in environment variables")

    mongo_client = get_mongo_client(mongo_uri)

    # Ingest data into MongoDB
    db = mongo_client[database]
    col = db[collection]

    return db
