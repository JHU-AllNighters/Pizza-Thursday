def _get_attendees(df, people_col):

    attendees = []

    for people in df[people_col]:
        if people == "All":
            continue

        for person in people.split(","):
            person = person.lstrip()
            if person in attendees:
                continue
            else:
                attendees.append(person)

    return attendees


def _get_individual_cost(df, name, people_col, price_col):

    subset = df[df[people_col].str.contains(name)]

    cost = 0

    for _, (price, people) in subset.iterrows():
        n_participants = len(people.split(","))
        cost += price / n_participants

    return cost


def _get_group_cost(df, cost_dict, people_col, price_col):

    # Get individual and group data sets
    individual = df.query(f"{people_col} != 'All'")
    group = df.query(f"{people_col} == 'All'")

    # Get total individual costs (the subtotal) and additional costs
    subtotal = sum(individual[price_col])
    additional = sum(group[price_col])

    # Proportionally add additional costs
    for person, cost in cost_dict.items():
        proportion_of_subtotal = cost / subtotal
        cost_dict[person] += proportion_of_subtotal * additional

    return cost_dict


def _make_pretty(cost_dict):
    for person, cost in cost_dict.items():
        cost_dict[person] = round(cost, 2)
    return cost_dict


def main(df, people_col, price_col):

    # Get attendees
    attendees = _get_attendees(df, people_col)

    # Estimate prelimary cost dictionary
    cost_dict = dict()
    for attendee in attendees:
        cost = _get_individual_cost(df, attendee, people_col, price_col)
        cost_dict[attendee] = cost

    # Include delivery fee, tax, and tip
    cost_dict = _get_group_cost(df, cost_dict, people_col, price_col)
    cost_dict = _make_pretty(cost_dict)

    return cost_dict
