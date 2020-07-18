class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    # hash the table to store route and destination info
    cache = {}
    # initialize list to store original source
    route = [None] * length

    # iterate through each ticket and store
    for t in tickets:
        cache[t.source] = t.destination

    # first ticket has None source
    dest = cache["NONE"]

    # iterate through each destination and add to array
    for flight in range(length):
        # record value
        route[flight] = dest

        dest = cache[dest]

    return route