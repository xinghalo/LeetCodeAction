select
    FirstName,
    LastName,
    City,
    State
from Person p
left join Address addr
on p.PersonId = addr.PersonId