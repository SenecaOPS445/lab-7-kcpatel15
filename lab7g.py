#!/usr/bin/env python3
# Student ID: kcpatel15 
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        total_seconds += t2.hour * 3600 + t2.minute * 60 + t2.second

        hour = total_seconds // 3600
        total_seconds %= 3600
        minute = total_seconds // 60
        second = total_seconds % 60

        return Time(hour, minute, second)

    def print_time(self):
        print(self.__str__())

    def format_time(self):
        return self.__str__()

    def sum_times(self, t2):
        return self.__add__(t2)
