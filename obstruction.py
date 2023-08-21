class OBS:
    def __init__(self, a:float, b:float):
        self.a = a
        self.b = b
        self.distance = self.a - self.b
    
    def there_is_or_no_obstruction(self, speed):
        time = self.distance / speed
        if time >= 60:
            return True
        return False