class WrongCharError(ValueError):
    def __init__(self):
        super().__init__()

class Menu:
    def __init__(self):
        self._commands = []
        self._should_running = True

    def add_command(self, cmd):
        self._commands.append(cmd)

    def run(self):
        while self._should_running:
            self._display_menu()
            self._execute_selected_command()

    def stop(self):
        self._should_running = False

    def _display_menu(self):
        for i, cmd in enumerate(self._commands):
            print("{}. {}".format(i + 1, cmd.description()))

    def _execute_selected_command(self):
        cmd_num = int(input("Select menu item (1-{}): ".format(len(self._commands))))

        cmd = self._commands[cmd_num - 1]
        cmd.execute()

class MenuCommand:
    def description(self):
        '''Return menu item name.'''
        raise NotImplementedError

    def execute(self):
        '''Code will be executed on menu action.'''
        raise NotImplementedError

class ExitCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self._menu.stop()

class NewEventCommand(MenuCommand):
    def __init__(self, calendar):
        super().__init__()
        self.calendar = calendar
        self.event = {}

    def description(self):
        return "New event"

    def execute(self):
        try:
            Title = input("Title: ")
            self.event["title"] = self.title_validator(Title)

            Date = input("Date (DD.MM.YYYY): ")
            self.event["date"] = self.date_validator(Date)

            Time = input("Time (HH:MM): ")
            self.event["time"] = self.time_validator(Time)

            self.calendar.append(self.event)

        except WrongCharError:
            print("Invalid input")


    def title_validator(self, title):
        valid_characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -,.'
        if all(char in valid_characters for char in title):
            return title
        else:
            raise WrongCharError



    def date_validator(self, date):
        # WSZYSTKIE DATY MUSZA BYC DWUCYFROWE
        try:
            day, month, year = date.split(".")
            if (len(year) >= 1 and len(year) <= 4):
                return date
            else:
                raise WrongCharError
        except ValueError:
            raise WrongCharError

    # DO DOROBIENIA OBLSUGA CHUJOWYCH DNI
    # https://codereview.stackexchange.com/questions/200634/program-to-check-if-a-date-is-valid-or-not
    # DO PRZEROBIENIA OBSLUGA CHUJOWYCH POLECEN

    def time_validator(self, time):
        # WSZYSTKIE Godziny i minuty MUSZA BYC DWUCYFROWE
        return time
        #try:
        #    hours, minutes = time.split(":")
        #    if (int(hours)<=0 and int(hours)<=24) and (int(minutes)<=0 and int(minutes)<=59):
        #        return time
        #    else:
        #        raise WrongCharError
        #except ValueError:
        #   raise WrongCharError


class ListCalendarCommand(MenuCommand):
    def __init__(self, context):
        super().__init__()
        self.context = context
        #mozna sprobowac zeby brala kalendarz i wtedy context jest czysty
    def description(self):
        return "List calendar"
    def execute(self):
        self.context.do_magic()




class ICalendarExportCommand(MenuCommand):
    def __init__(self,context):
        super().__init__()
        self.context = context

    def description(self):
        return "Export calendar to iCalendar"

    def execute(self):
        self.context.do_magic()


