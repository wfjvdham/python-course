import math


train_stations = {
    "Amsterdam": {
         "coordinates": [52.3791283, 4.8980833],
         "connections": ["Rotterdam", "Utrecht"]
        },
    "Rotterdam": {
        "coordinates": [51.92235, 4.4661983],
        "connections": ["Amsterdam", "Utrecht"]
    },
    "Utrecht": {
        "coordinates": [52.0894444, 5.1077981],
        "connections": ["Amsterdam", "Rotterdam", "Arnhem", "Oberhausen"]
    },
    "Arnhem": {
        "coordinates": [51.984034, 5.8983483],
        "connections": ["Utrecht", "Oberhausen"]
    },
    "Oberhausen": {
        "coordinates": [51.4983534, 6.8131958],
        "connections": ["Arnhem", "Utrecht"]
    }
}


def latitude(coordinates):
    return coordinates[0]


def longitude(coordinates):
    return coordinates[1]


def meters_to_kilometers(meters):
    return meters / 1000


def distance_in_meters(coord1, coord2):
    """This function does not contains any errors ;)"""
    earth_radius_in_meters = 6371000

    def radians(degrees):
        return math.pi / 180 * degrees

    delta_latitude = radians(latitude(coord2) - latitude(coord1))
    delta_longitude = radians(longitude(coord2) - longitude(coord1))
    a = (math.sin(delta_latitude / 2)
         * math.sin(delta_latitude / 2)
         + math.cos(radians(latitude(coord1)))
         * math.cos(radians(latitude(coord2)))
         * math.sin(delta_longitude / 2)
         * math.sin(delta_longitude / 2))

    c = math.atan2(math.sqrt(a), math.sqrt(1 - a)) * 2

    return earth_radius_in_meters * c


def distance_between_stations_in_meters(station1, station2):
    return distance_in_meters(station1['coordinates'], station2['coordinates'])


def departure(route):
    return route[0]


def destination(route):
    return route[route.length - 1]


def is_in_route(route, city):
    return city in route


def update_route(route, city):
    new_route = route[:]
    new_route.append(city)
    return new_route


def routes(departing_city, destination_city):
    if departing_city == destination_city:
        raise Exception("Destination city cannot be the same as departure city.")

    possible_routes = []

    def build_routes(route):
        current_city = route[len(route) - 1]
        current_station = train_stations[current_city]
        for connected_city in current_station['connections']:
            if not is_in_route(route, connected_city):
                updated_route = update_route(route, connected_city)
                if connected_city == destination_city:
                    # stop, we arrived
                    possible_routes.append(updated_route)
                else:
                    build_routes(updated_route)

    starting_route = [departing_city]
    build_routes(starting_route)
    return possible_routes


def route_length_in_kilometers(route):
    if len(route) < 2:
        return 0
    else:
        total_length_in_km = 0
        for current_city, next_city in zip(route, route[1:]):
            current_station = train_stations[current_city]
            next_station = train_stations[next_city]
        # for index, current_city in enumerate(route):
        #     if index == len(route) - 1:
        #         break
        #     current_city = route[index]
        #     current_station = train_stations[current_city]
        #     next_city = route[index + 1]
        #     next_station = train_stations[next_city]
            total_length = distance_between_stations_in_meters(current_station, next_station)
            total_length_in_km += meters_to_kilometers(total_length)
        return total_length_in_km


def shortest_route(routes):
    if len(routes) == 0:
        raise Exception("There must be at least one route")
    else:
        current_shortest_route = routes[0]
        for route in routes:
            if route_length_in_kilometers(current_shortest_route) > route_length_in_kilometers(route):
                current_shortest_route = route

        return current_shortest_route


def route_cost_in_euros(route):
    price_per_kilometers = 0.19
    return route_length_in_kilometers(route) * price_per_kilometers


amsterdam_arnhem_routes = routes("Amsterdam", "Arnhem")
print(amsterdam_arnhem_routes)
shortest_amsterdam_arnhem_route = shortest_route(amsterdam_arnhem_routes)

print("Our route: %s is %.2f km costing %.2f euros" % (shortest_amsterdam_arnhem_route,
                                                       route_length_in_kilometers(shortest_amsterdam_arnhem_route),
                                                       route_cost_in_euros(shortest_amsterdam_arnhem_route)))

