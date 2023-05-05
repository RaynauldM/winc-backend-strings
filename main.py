# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

score1 = 'Ruud Gullit'
score2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

scorers = score1 + ' ' +  str(goal_0) + ', ' + score2 + ' '  + str(goal_1)

report = f'{score1} scored in the {goal_0}nd minute\n{score2} scored in the {goal_1}th minute'

# on to part two

player = 'Jan Wouters'

first_name = player[0:player.find(' ')]

last_name = player[player.find(' ')+1:]

last_name_len = len(last_name)

name_short = f'{player[0]}. {last_name}'

first_chant = (first_name + '!' + ' ') * len(first_name)

chant = first_chant[:-1]

good_chant = chant[-1] != ' '







