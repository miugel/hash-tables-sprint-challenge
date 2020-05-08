class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

def reconstruct_trip(tickets, length):
    hash_table = {}

    for i in tickets:
        hash_table[i.source] = i.destination
    
    route = [None] * length
    route[0] = hash_table['NONE']

    for i in range(1, len(route)):
        route[i] = hash_table[route[i-1]]

    # print(route)
    return route

# tickets = [
#     Ticket("PIT", "ORD"),
#     Ticket("XNA", "CID"),
#     Ticket("SFO", "BHM"),
#     Ticket("FLG", "XNA"),
#     Ticket("NONE", "LAX"),
#     Ticket("LAX", "SFO"),
#     Ticket("CID", "SLC"),
#     Ticket("ORD", "NONE"),
#     Ticket("SLC", "PIT"),
#     Ticket("BHM", "FLG")
# ]

# reconstruct_trip(tickets)