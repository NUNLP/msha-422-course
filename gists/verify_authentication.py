import os


def main():
    from google.cloud import storage

    # If you don't specify credentials when constructing the client, the
    # client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


if __name__ == "__main__":
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = \
        "/Users/willthompson/Code/wkt/msha/MSHA-422-565648ed8982.json"
    main()

