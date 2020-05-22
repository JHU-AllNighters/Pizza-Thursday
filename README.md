# Pizza Thursday
Every Thursday night, the AllNighters (JHU's best-smelling all-male a cappella group) order pizza! Since one person usually pays, figuring out how much each attendee owes is a tedious task. Now, we can algorithmically determine the appropriate Venmo requests for Pizza Thursdays!

## Data
Costs are tabulated in a simple Google sheet. They are read into Python using Pandas.

## Algorithm
- Use some fancy Pandas operations to calculate the cost per person.
- Each person contributes proportionally to group costs (such as Tip, Taxes, and Delivery Fee).
