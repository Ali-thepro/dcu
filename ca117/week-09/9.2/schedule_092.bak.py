#!/usr/bin/env python3

class Meeting(object):

    def __init__(self, hour, minute, duration):
        self.hour = hour
        self.minute = minute
        self.duration = duration

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"

def tagger(item):
    return item.hour, item.minute
class Schedule(object):

    def __init__(self):
        self.meetings = []

    def add(self, m):
        self.meetings.append(m)

    def __str__(self):
        output = []
        output.append("Schedule")
        output.append("--------")
        for v in sorted(self.meetings, key=tagger):
            output.append(f'{v}')
        output.append(f"Meetings today: {len(self.meetings)}")
        return "\n".join(output)





# class Meeting(object):

#     def __init__(self, hour, minute, duration):
#         self.hour = hour
#         self.minute = minute
#         self.duration = duration

#     def __str__(self):
#         return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"


# class Schedule(object):

#     def __init__(self, meetings=None):
#         self.meetings = {} if meetings is None else meetings

#     def add(self, m):
#         if m.hour not in self.meetings:
#             self.meetings[m.hour] = m

#     def __str__(self):
#         output = []
#         output.append("Schedule")
#         output.append("--------")
#         for k, v in sorted(self.meetings.items()):
#             output.append(f'{v}')
#         output.append(f"Meetings today: {len(self.meetings)}")
#         return "\n".join(output)








# class Meeting(object):

#     def __init__(self, hour, minute, duration):
#         self.hour = hour
#         self.minute = minute
#         self.duration = duration
        
#     def __str__(self):
#         return f"{self.hour:02d}:{self.minute:02d} ({self.duration} minutes)"
    


# class Schedule(object):

#     def __init__(self):
#         self.list = []

#     # def __init__(self, list=None):
#     #     self.list = [] if list is None else list

#     def add(self, meeting):
#         if meeting not in self.list:
#             self.list.append(str(meeting))

#     def __str__(self):
#         output = []
#         output.append("Schedule")
#         output.append("--------")
#         for line in sorted(self.list):
#             output.append(f'{line}')
#         output.append(f"Meetings today: {len(self.list)}")
#         return "\n".join(output)
    





# class Schedule(object):

#     def __init__(self, meetings=None):
#         self.meetings = {} if meetings is None else meetings

#     def add(self, m):  # using the __str__ method return value as key
#         self.meetings[m.__str__()] = m

#     def __str__(self):
#         output = ["Schedule", "--------"]
#         for m in sorted(self.meetings):
#             output.append(self.meetings[m].__str__())
#         output.append(f"Meetings today: {len(self.meetings)}")
#         return "\n".join(output)





    # def __str__(self):
    #     schedule_list = [str(m) for m in self.meetings]       self.meetings is a list
    #     schedule_list.append(f'Meetings today: {len(schedule_list)}')
    #     return '\n'.join(['Schedule', '--------'] + sorted(schedule_list))



    # def __str__(self):
    #     lines = []
    #     lines.append('Schedule')
    #     lines.append('--------')
    #     for h, m in sorted(self.meet.items()):
    #         lines.append(Meeting.__str__(m))
    #     lines.append('Meetings today: {}'.format(len(lines) - 2))
    #     return '\n'.join(lines)