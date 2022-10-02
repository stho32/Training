# "split", Splitting costs in a group of people

Imagine you go on holidays in a group. 

- There are always expenses, and there is always someone that pays.
- Some expenses are for more than one person. (E.g. Bob buys food for everyone).
- The costs need to be splitted.

Write an application that can return the amount of money each person ows any other person in the group.

It should return a list of payments and who has to pay whom to equally distribute all expenses throughout the group.

## Examples

- You drive together in a car. Cost for gas is 50 EUR. You are 5 people. You are Bob. Bob has payed. The result should read something like:

"OtherGuy1 : pay 10 EUR to Bob.
OtherGuy2 : pay 10 EUR to Bob.
OtherGuy3 : pay 10 EUR to Bob.
OtherGuy4 : pay 10 EUR to Bob."

- You have another expense. You stop by a pizza store. OtherGuy2 buys a pizza and shares it with Bob. Cost for the pizza 10 EUR.

The result is now: 
"OtherGuy1 : pay 10 EUR to Bob.
OtherGuy2 : pay 5 EUR to Bob.
OtherGuy3 : pay 10 EUR to Bob.
OtherGuy4 : pay 10 EUR to Bob."

- You have another expense. OtherGuy4 pays for the hotel room. 100 EUR. 

... now Bob owes OtherGuy4 something, right?
