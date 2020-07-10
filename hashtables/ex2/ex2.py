#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def __str__(self):
        return f'Source: {self.source} - Destination: {self.destination}'


def reconstruct_trip(tickets, length):

    trip_cache = {}
    route = []

    for ticket in tickets:
        trip_cache[ticket.source] = ticket.destination

    next_destination = trip_cache['NONE']

    while next_destination != 'NONE':
        route.append(next_destination)
        next_destination = trip_cache[next_destination]
    route.append('NONE')
    print(route)

    return route
