#League of Legends Rank up calcuator
#Calculates how many games it will take a user ro reach their desired rank from their current rank
#Uses a baseline of +/-22 LP and user inputed winrate

#List of rank names as strings
ranks_list = ["unranked", "iron4", "iron3", "iron2", "iron1", "bronze4",
"bronze3", "bronze2", "bronze1", "silver4", "silver3", "silver2",
"silver1", "gold4", "gold3", "gold2", "gold1", "platinum4", "platinum3",
"platinum2", "platinum1", "diamond4", "diamond3", "diamond2",
"diamond1", "masters"]

print("Hello Summoner!")
print("Let's determine how many games you need to play to hit your ranked goal this season.)")
print("(Note: this calculator only works for Masters and below")

goal_lp = -100
lp = -100
rank = input("What's your current rank? (Enter as 'iron4', 'platinum3', etc.)").lower()
while rank not in ranks_list:
    rank = input("Please enter a valid rank").lower()

for i in ranks_list:
    if rank == "unranked":
        print("So, you haven't done your placements yet?")
        rank = input("Well, what were you ranked last season then?").lower()
        while rank not in ranks_list:
            rank = input("Please enter a valid rank").lower()
        lp += 100
    elif rank != i:
        lp += 100
    else:
        break


bonus_lp = input("How much LP do you currently have?")

while bonus_lp.isdigit() == False or int(bonus_lp) >= 100:
    bonus_lp = input("Please enter a valid number")
lp += int(bonus_lp)

print("So you're currently", rank, bonus_lp, "LP?")

goal_rank = input("What's your target rank?").lower()
while goal_rank not in ranks_list:
    rank = input("Please enter a valid rank").lower()

for x in ranks_list:
    if goal_rank == "unranked":
        print("If your goal is to be unranked, you're in the wrong place")
        goal_rank = input("Please enter a valid rank").lower()
        while goal_rank not in ranks_list:
            goal_rank = input("Please enter a valid rank").lower()
        goal_lp += 100
    elif goal_rank != x:
        goal_lp += 100
    else:
        break


need_lp = goal_lp - lp

champ = input("What champion are you planning on climbing with?").title()
wr = float(input("What is your win rate playing them?"))
print("So you have a", str(wr)+"% win rate", "playing", str(champ)+"?")

lp_ratio = 22 * (wr - (100 - wr))/100
games_needed = "{:.0f}".format(need_lp / lp_ratio)


print("Assuming you maintain a", str(wr)+"% winrate on", champ, "and have an MMR equal to your current rank,")
print("It should take you about", int(games_needed) - 4, "to", int(games_needed) + 4, "to reach", goal_rank, "from", str(rank)+".") 
