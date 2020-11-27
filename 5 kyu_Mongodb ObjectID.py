from datetime import datetime


class Mongo(object):

    @classmethod
    def is_valid(cls, s):
        """returns True if s is a valid MongoID; otherwise False"""
        if isinstance(s, str) and not(any(letter.isupper() for letter in s)) and len(s) == 24:
            try:
                int(s, 16)
                return True
            except ValueError:
                return False
        return False

    @classmethod
    def get_timestamp(cls, s):
        """if s is a MongoID, returns a datetime object for the timestamp; otherwise False"""
        if Mongo.is_valid(s):
            seconds = int(s[:8], 16)
            return datetime.fromtimestamp(seconds)
        return False


print(Mongo.is_valid('507f1f77bcf86cd799439016'))
print(Mongo.get_timestamp('111111111111111111111111'))