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
        try:
            cmd_num = int(input("Select menu item (1-{}): ".format(len(self._commands))))
            if cmd_num not in range(1,len(self._commands)):
                raise WrongCharError
            cmd = self._commands[cmd_num - 1]
            cmd.execute()
        except (ValueError, WrongCharError):
            print("Invalid input")

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
        self.calendar = calendar

    def description(self):
        return "New event"

    def execute(self):
        event = {}
        try:
            Title = input("Title: ")
            event["title"] = self.title_validator(Title)

            Date = input("Date (DD.MM.YYYY): ")
            event["date"] = self.date_validator(Date)

            Time = input("Time (HH:MM): ")
            event["time"] = self.time_validator(Time)

            self.calendar.append(event)

        except WrongCharError:
            print("Invalid input")

    def title_validator(self, title):
        valid_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -,."
        if all(char in valid_characters for char in title):
            return title
        else:
            raise WrongCharError

    def date_validator(self, date):

        def day_validator(day, month):
            monthlist31 = [1, 3, 5, 7, 8, 10, 12]
            monthlist30 = [4, 6, 9, 11]
            monthlist28 = 2

            if int(day) >= 1:
                if int(month) in monthlist31 and int(day) <= 31:
                    return True
                elif int(month) in monthlist30 and int(day) <= 30:
                    return True
                elif int(month) == monthlist28 and int(day) <= 28:
                    return True
            else:
                return False

        try:
            day, month, year = date.split(".")
            date_len_valid = len(day) == 2 and len(month) == 2 and 1 <= len(year) <= 4
            month_valid = 1 <= int(month) <= 12
            day_valid = day_validator(day, month)

            if date_len_valid and month_valid and day_valid:
                return date
            else:
                raise WrongCharError

        except ValueError:
            raise WrongCharError

    def time_validator(self, time):
        try:
            hours, minutes = time.split(":")
            time_len_valid = len(hours) == 2 and len(minutes) == 2
            hours_range_valid = 0 <= int(hours) <= 23
            minutes_range_valid = 0 <= int(minutes) <= 59

            if time_len_valid and hours_range_valid and minutes_range_valid:
                return time
            else:
                raise WrongCharError

        except ValueError:
            raise WrongCharError

class ListCalendarCommand(MenuCommand):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def description(self):
        return "List calendar"

    def execute(self):
        self.context.do_magic()

class ICalendarExportCommand(MenuCommand):
    def __init__(self, context):
        super().__init__()
        self.context = context

    def description(self):
        return "Export calendar to iCalendar"

    def execute(self):
        self.context.do_magic()
