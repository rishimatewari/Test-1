height = 7
width = 2 * height - 1
trunk = 3
tt = 3
for counter in range(height):
    num_stars = (2 * counter + 1)
    total_spaces = width - num_stars
    print (total_spaces/2)*" "+ num_stars*"*"

for counter in range(trunk):
    print ((width-tt)/2)*" " + tt*"*"
