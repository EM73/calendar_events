'''
W tym pliku znajdziesz kod odpowiedzialny za wyświetlanie zdarzeń z kalendarza.

Do zmiany zachowania funkcji list_calendar wykorzystaj strategię ListingStrategy.

Tego pliku nie musisz zmieniać.
'''

class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass


def list_calendar(calendar, listing_strategy):
    print(calendar)
    listing_strategy.begin()

    for event in calendar:
        title = event['title']
        date = event['date']
        time = event['time']
        print(event)
        listing_strategy.event(title, date, time)

    listing_strategy.end()
