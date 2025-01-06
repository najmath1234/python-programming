import datetime

class Time:
    def __init__(self):
        time_entry = input("Enter a time in hh:mm:ss format: ")
        self.__hours, self.__minutes, self.__seconds = map(int, time_entry.split(":"))
        print(f"Time entered: {self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}")
        
    def __add__(self, other):
        self.seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        other.seconds = other.__hours * 3600 + other.__minutes * 60 + other.__seconds
        return self.convert(self.seconds + other.seconds)
    
    def convert(self, seconds):
        seconds = seconds % (24 * 3600)  # to handle wrapping around a 24-hour format
        hours = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# Example usage:
t1 = Time()
t2 = Time()
print("Sum of times:", t1 + t2)

    
