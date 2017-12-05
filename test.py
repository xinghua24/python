class Time:
    """Represents the time of day.
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))


if __name__ == '__main__':
    time = Time(5,30,0)
    time.print_time()
