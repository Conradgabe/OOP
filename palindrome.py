class Palindrome:
    """
    Palindrome Module to check if arguments are palindrome.
    
    parameters:
    [*args] : Any
    """
    def __init__(self):
        pass

    # staticmethod to compare palindrome Strings
    @staticmethod
    def is_string_palindrome(p_args):
        return p_args == p_args[::-1] # Returns True or False if args is a palindrome
    
    # staticmethod to compare palindrome integers 
    @staticmethod
    def is_integer_palindrome(p_args):
        temp_p_args = p_args # assign the palindrome args to temp value
        temp_int_reversed = 0
        while temp_p_args != 0:
            temp_modulo = temp_p_args % 10 # Get the last int value

            temp_int_reversed *= 10 
            temp_int_reversed += temp_modulo

            temp_p_args = temp_p_args // 10 # Removes the last value and assigns the remaining to temp_p_args

        return p_args == temp_int_reversed
    
    # Classmethod, accepts a variable number of arguments and checks if arguments are valid and are palindrome
    # Appends them to list and then prints them.
    @classmethod
    def check_for_palindrome(cls, *args):
        palindrome = list()
        for arg in args:
            
            #Check if the args is a String or a sentence and append to list
            if isinstance(arg, str):
                p_array = arg.split(" ")
                for values in p_array:
                    if cls.is_string_palindrome(values):
                        palindrome.append(values)
                    else:
                        pass

            # Check if the args is an Integer and append to list
            elif isinstance(arg, int):
                if cls.is_integer_palindrome(arg):
                    palindrome.append(arg)
                else:
                    pass
            
            # If type doesn't match Return error
            else:
                return {"Error": f"Input value of type {type(arg)} is an invalid type"}
        
        # Prints the list of values in tbe palindrome list
        for values in palindrome:
            print(values, end=" ")

        return palindrome
    
if __name__ == "__main__":
    palindrome = Palindrome()
    palindrome.check_for_palindrome(1230321, "radar", 87988, "hello")
    print("---")
    palindrome.check_for_palindrome("230321 radar", 87988, "hello")
    print("---")
    palindrome.check_for_palindrome("1230321 radar 87988", "hello")
    print("---")
    palindrome.check_for_palindrome("1230321 radar 87988 hello")
    print("---")
    palindrome.check_for_palindrome(1230321, 87988978, 9900007000099)
    print("---")
    palindrome.check_for_palindrome(1230321, 9234, 0o124210, 1230321, 0o124210)
    print("---")
    palindrome.check_for_palindrome('returns')
    print("---")
    palindrome.check_for_palindrome("abcd5dcba", 1230321, 9234, 0o124210)
    print("---")
    palindrome.check_for_palindrome('cccccc')
    print("---")
    palindrome.check_for_palindrome("my name is isi and i am in level two")
    print("---")
    palindrome.check_for_palindrome(",,,i,")
    