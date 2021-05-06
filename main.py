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
        list_event = "Title: %s \n Date: %s, %s" %(title, date, time)
        print(list_event)

class ICalendarExport(ListingStrategy):
    pass


def main():
    # wydarzenia przechowuj w liście
    calendar = []
    menu = Menu()

    new_event = NewEventCommand(calendar)
    menu.add_command(new_event)


    context = Strategy(calendar, SimpleList())


    menu.add_command(ListCalendarCommand(context))

    menu.add_command(ICalendarExportCommand(calendar))

    menu.add_command(ExitCommand(menu))

    menu.run()

main()
