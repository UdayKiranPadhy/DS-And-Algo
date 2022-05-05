from functools import lru_cache

class UserMainCode(object):
    @classmethod
    def arrangements(cls,input1):

        @lru_cache(None)
        def count(number):
            if number == 1:
                return 0
            if number == 2:
                return 1
            return (number-1)* (count(number-1) + count(number-2))
        
        return count(input1)