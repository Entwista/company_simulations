# Lets start with 1 location
# We need to buy food, prepare food, sell food, and clean the restaurant

# Lets say that we have only one item on the menu, burgers, and they take a fixed amount of time to make
BURGERS_PER_HOUR = 12

# Lets say that employees have certain wages
HOURLY_WAGE = 15

# Lets say that burgers have a price
BURGER_PRICE = 5

# Now we can calculate the profit that we should make per burger, with only these costs
profit_margin_per_burger = BURGER_PRICE - HOURLY_WAGE / BURGERS_PER_HOUR

assert profit_margin_per_burger == 3.75

# Lets say that we get 10 customers per hour, and employee this one employee for 8 hours a day
CUSTOMERS_PER_HOUR = 10
OPENING_HOURS = 8

# You can't serve more customers than you get, or than your cook can handle
def profit(customers_per_hour=0, max_burgers_per_hour=0):
    customers_served = min(customers_per_hour, max_burgers_per_hour)
    revenue = customers_served * OPENING_HOURS * BURGER_PRICE
    costs = HOURLY_WAGE * OPENING_HOURS
    profit = revenue - costs
    return profit
assert profit(customers_per_hour=10, max_burgers_per_hour=12) == 280

# Whats the maximum amount of profit we could make per day with one employee?
assert profit_margin_per_burger * (OPENING_HOURS * BURGERS_PER_HOUR) == 360

# Logically, we will make this profit if we get at least as many customers to keep our cook completely busy
assert profit(customers_per_hour=12, max_burgers_per_hour=12) == 360

# If we get more customers it does nothing for us:
assert profit(customers_per_hour=100, max_burgers_per_hour=12) == 360

# Now lets think about how we can introduce issues with principal agent problems, the core issues
# with agents are that they are difficult to incentivise for the global outcome as well as the long term outcome
# You can pay an agent only in shares in the business, which gives them a long term focus, you can also pay them
# based on performance, but unless they control the whole business, this gives them a local focus. 

# Lets try paying the cook based on the amount of burgers they make per hour. The cook now has an incentive to make
# more burgers, so it would be reasonable to expect them to do so, however, whereas before they had no incentive to cut 
# corners on quality, they now definitely do

# Lets say they can make more burgers per hour if they sacrifice quality
LOW_QUALITY_BURGERS_PER_HOUR = 20

# However, low quality burgers cause an unobserved cost to the business, lets create a quantity called reputation
reputation = 1000

# Lets say every day that we make low quality burgers, reputation falls by a point
profit_made = []
for day in range(1000):
    reputation -= 1
    daily_profit = profit(customers_per_hour=reputation/25, max_burgers_per_hour=LOW_QUALITY_BURGERS_PER_HOUR)
    profit_made.append(daily_profit)

# On the 0th day, we get more money, because we still have our reptuation
assert profit_made[0] == (BURGER_PRICE * LOW_QUALITY_BURGERS_PER_HOUR - HOURLY_WAGE) * OPENING_HOURS == 680

# On the 500th day our reputation has dropped to the point where as start making slightly less money
assert 670 < profit_made[500] < 680

assert 278 < profit_made[750] < 279

# On day 925 we are losing money
assert profit_made[925] < 0

# After that point the losses get worse until the simulation ends
assert profit_made[999] == -120

# If we own the above business, how should we proceed? Clearly over the long term our strategy of the financial
# incentive didn't work, and as we can't see reputation directly it would have been impossible for an observer
# of the accounting figures to realise what is going on, they instead would have seen 500 days of increased profits
# before seeing a gradual decline, if a highly attentive business owner went looking for changes around the time of the 
# decline, they would miss the culprit, as nothing has changed in the way the business operates in the last 500 days.