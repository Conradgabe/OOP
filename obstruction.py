class OBS:
    """
    Checks to see if there are any obstruction between a to b
    """
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
        self.distance = self.a - self.b # calculates the distance between a and b
    
    # checks to see if obstruction, takes in 1 parameter 'speed'
    # then calculate for the time
    def there_is_or_no_obstruction(self, speed):
        time = self.distance / speed
        # if time duration to go from point 
        # a to b exceeds 60 minutes then the rocks are impenetrable
        if time >= 60:
            return True
        return False
    
if __name__ == "__main__":
    obs = OBS()