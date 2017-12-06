class Time:
    """Represents the time of day.
    attributes are hour, minute and second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

if __name__ == '__main__':
    time = Time(5,30,0)
    print(time)
