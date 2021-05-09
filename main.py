from menu import Menu, MenuCommand, ExitCommand, NewEventCommand, ListCalendarCommand, ICalendarExportCommand
from calendar import ListingStrategy, list_calendar


class Strategy:
    def __init__(self, calendar, strategy):
        self.calendar = calendar
        self.strategy = strategy

    def do_magic(self):
        return list_calendar(self.calendar, self.strategy)

class SimpleList(ListingStrategy):
    def event(self, title, date, time):
        list_event = "Title: %s \nDate: %s, %s" % (title, date, time)
        print(list_event)

class ICalendarExport(ListingStrategy):
    def __init__(self):
        self.header = "BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE\n"
        self.footer = "END:VCALENDAR"
        self.counter = 0

    def begin(self):
        print(self.header, end="")

    def event(self, title, date, time):
        day, month, year = date.split(".")
        hour, minutes = time.split(":")
        ical_time = f"{year}{month}{day}T{hour}{minutes}00"
        ical_event = f"BEGIN:VEVENT\nDTSTART:{ical_time}\nDTEND:{ical_time}\nSUMMARY:{title}\nEND:VEVENT"

        #if self.counter == 0:
        #    print(self.header, end="")
        #self.counter += 1

        print(ical_event)

    def end(self):
        print(self.footer)


def main():
    calendar = []
    menu = Menu()


    menu.add_command(NewEventCommand(calendar))

    context = Strategy(calendar, SimpleList())
    menu.add_command(ListCalendarCommand(context))

    context = Strategy(calendar, ICalendarExport())
    menu.add_command(ICalendarExportCommand(context))

    menu.add_command(ExitCommand(menu))

    menu.run()


main()
