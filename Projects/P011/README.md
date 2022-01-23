# Create an app that helps you buy the right ingredients for a set of meals you want to eat

This app is there to help you with most of your weekly grocery shopping.

Hint: you have a set of simple recipies in the docs.

There are the following additional common rules that apply: 
https://github.com/stho32/Collection-Of-Challenges/blob/master/Common-Requirements.md

## Requirements

### Level 1
- [ ] (R001) there is a way to select one recipe and the app will print out the needed ingredients
- [ ] (R002) a recipe can be selected multiple times
- [ ] (R003) you can select multiple different recipes, too
- [ ] (R004) find a way where there is a kind of table with every day of the week on it and you can select the breakfast, dinner and supper for every day
- [ ] (R005) when there are more than 1 recipe selected the app will calculate the amount of stuff you need to have

### Level 2
- [ ] (R006) Create an algorithm that creates a random selection for the week for every meal you need.
- [ ] (R007) You might need a way to increase or decrease the number of people that you cook for.
- [ ] (R008) There are recipes that are more suited for breakfast, or more suited for dinner, or more suited for supper. They should be put in there accordingly.
- [ ] (R009) There are null-recipes, like, when you go to dinner in a restaurant. 
- [ ] (R010) There are recipes that have nothing to do with food. E.g. cleaning agents. Add a recipe that contains a list of that so you keep track of those things too.

### Level 3
- [ ] (R011) Find a way to check against you current stock. What ingredients do you already have and in what amount? Reduce the amount you need to buy by what you already have.
- [ ] (R012) Find a way to get your shopping list onto your phone, so you can take it with you into the store
- [ ] (R013) When buying ingredients look out for the following sub-problems:
  - [ ] (R014) Ingredients are not products. Translate the ingredients to products for at least 2 different stores. How much of each *product* do you need to buy?

### Level 4
- [ ] (R015) Find an algorithm or algorithms to optimize the selection of meals for:
  - [ ] (R016) Minimal total cost (you should not create much garbage, all ingredients should be used)
    - [ ] (R017) You might want to have a parameter that allows you to select how many grocery stores you want to visit. Not everything is of same price everywhere. When you buy all the stuff in one store you might end up with a higher price but you save time.
  - [ ] (R018) Not all ingredients last long. Find an optimization that helps you use all ingredients before they expire.
    - [ ] (R019) If you want to do that correctly you might want to start the "random selection of meals" with a report on what you have on stock and use those ingredients first.
  - [ ] (R020) You should not have many repetitions of meals during a 2 week cycle. 
  
### Level 5
- [ ] (R021) Let the app write its own history. What did it recommend when. What did you have in stock.
- [ ] (R022) Enter and save what you bought.
- [ ] (R023) From the history, information about what you bought and their expiration dates, and the remaining stock information the app should be able to give you automatic follow up proposals what to eat and buy next without requiring you to configure a lot.



