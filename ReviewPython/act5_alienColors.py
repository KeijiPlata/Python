# Activity 5-3 alien colors

# assigning a color of green to alien_color
alien_color = 'green'
score = 0
if alien_color == 'green':
    score += 5
    print("You just earned 5 points!")

# creating again the statement above but it should fail or no output
# this shit fails because it doesn't match the condition
alien_color = 'red'
score = 0
if alien_color == 'green':
    score += 5
    print("You just earned 5 points!")
