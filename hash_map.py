class HashTable:

    # Create empty bucket list of given size
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for _ in range(size)]

    def get_hash(self, key):
        return hash(key) % self.size

    def has(self, key):
        hashed_key = self.get_hash(key)
        bucket = self.hash_table[hashed_key]
        for record in bucket:
            if record[0] == key:
                return True
        return False

    # Insert value into hash map
    def add(self, key, val):

        # Get index from key
        hashed_key = self.get_hash(key)

        # Get bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        key_found = False
        for index, record in enumerate(bucket):

            # Check if bucket already contains key
            if record[0] == key:
                key_found = True
                break

        # Update if key exists, otherwise append
        if key_found:
            bucket[index] = (key, val)
        else:
            bucket.append((key, val))

    # Return searched value with specific key
    def get(self, key):

        # Get index from key
        hashed_key = self.get_hash(key)

        # Get bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        key_found = False
        for record in bucket:

            # Check if bucket contains key
            if record[0] == key:
                key_found = True
                break

        # If bucket contains key, return val
        if key_found:
            return record[1]
        else:
            return "No record found"

    # Remove a value with specific key
    def delete(self, key):

        # Get the index from the key using
        # hash function
        hashed_key = self.get_hash(key)

        # Get the bucket corresponding to index
        bucket = self.hash_table[hashed_key]

        key_found = False
        for index, record in enumerate(bucket):

            # Check if bucket contains key
            if record[0] == key:
                key_found = True
                break

        if key_found:
            bucket.pop(index)

        return


    def __str__(self):
        return "".join(str(item) for item in self.hash_table)
