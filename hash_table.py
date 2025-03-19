import logging

"""Create a logger for this python module"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s : %(levelname)s : %(message)s')

logger = logging.getLogger(__name__)


class HashTable:
    def __init__(self, size=10):
        """Initializing the hash table with empty lists (buckets)"""
        self.size = size
        self.count = 0
        """List comprehension"""
        # We will create a table that has n number of empty lists, n = size
        self.table = [[] for _ in range(size)]  # [[] ,[], [], [], []...]
        logger.debug(f"hash_table {self.table}")

    def _hash(self, key):
        """Hash function, returns an index for the key"""
        logger.debug(f"hash: {hash(key)} index = {self.size}")
        return hash(key) % self.size

    def _resize(self):
        """Resize the hash table"""
        load_factor = self.count / self.size
        logger.debug(f"Load factor: {load_factor}")
        if load_factor > 0.7:
            logger.debug("> 0.7 ")
            new_size = self.size * 2
            new_table = [[] for _ in range(new_size)]

            for bucket in self.table:
                for key, value in bucket:
                    new_index = hash(key) % new_size
                    new_table[new_index].append((key, value))

            self.size = new_size
            self.table = new_table
            logger.debug(f"new table: {new_table}")
    
    def search(self, key):
        """Search for key in hash table"""
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def insert(self, key, value):
        """Insert the data into the hash table"""
        index = self._hash(key)
        logger.debug(f"index after hash: {index}")
        key_exists = False
        # Check if key exists
        for idx, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][idx] = (key, value)
                key_exists = True
                break

        if not key_exists:
            self.table[index].append((key, value))
            self.count += 1
        
        self._resize()

    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                logger.info(f"Index {i}: Bucket: {bucket}")


hash_table = HashTable()

# Insert key-value pairs
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")
hash_table.insert("job", "Engineer")
hash_table.insert("country", "USA")

hash_table.display()
