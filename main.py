from menu import Menu, MenuCommand, ExitCommand, NewEventCommand, ListCalendarCommand, ICalendarExportCommand
from calendar import ListingStrategy, list_calendar

#
# w tym miejscu możesz napisać kod odpowiedzialny za menu (polecenia)
# i strategie wyświetlania wydarzeń z kalendarza
#
class Navigator():
    @staticmethod
    -> wyswietla
    ->grupuje

    def request(strategy):
        "The request is handled by the class passed in"
        return strategy()

    def result(self, strategy):
        list_calendar()
class CuteList(ListingStrategy):
    def __init__(self):
        super().__init__()

    def event(self, title, date, time):
        cute_list = "Title: %s \n Date: %s, %s" %(title, date, time)
        print(cute_list)
        return cute_list


class ICalendarExport:
    pass


def main():
    # wydarzenia przechowuj w liście
    calendar = []
    menu = Menu()

    new_event = NewEventCommand(calendar)
    menu.add_command(new_event)

    cute_list = list_calendar(calendar, CuteList())
    menu.add_command(ListCalendarCommand(cute_list))

    menu.add_command(ICalendarExportCommand())

    menu.add_command(ExitCommand(menu))

    menu.run()

main()
