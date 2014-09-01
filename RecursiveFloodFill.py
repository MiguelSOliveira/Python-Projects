import sys
textmap = """
....................
.......XXXXXXXXXX...
.......X........X...
.......X........X...
..XXXXXX........X...
..X.............X...
..X.............X...
..X........XXXXXX...
..X........X........
..XXXX..XXXX........
.....XXXX...........
....................
....................
"""

lines = textmap.strip().split('\n')
height = len(lines)
width = len(lines[0])
def getWorldFromText():
	world = []
	for x in xrange(width):
		world.append([''] * height)
	for x in xrange(width):
		for y in xrange(height):
			world[x][y] = lines[y][x]
	return world

def printWorld(world):
	for x in xrange(height):
		for y in xrange(width):
			sys.stdout.write(world[y][x])
		print

def fillWorld(world, x, y, oldCharacter, newCharacter):
	if oldCharacter == None:
		oldCharacter = world[x][y]

	if oldCharacter != world[x][y]:
		return

	world[x][y] = newCharacter
	if x > 0:
		fillWorld(world, x-1, y, oldCharacter, newCharacter) # left
	
	if x < width -1:
		fillWorld(world, x+1, y, oldCharacter, newCharacter) # right

	if y > 0:
		fillWorld(world, x, y-1, oldCharacter, newCharacter) # up

	if y < height - 1:
		fillWorld(world, x, y+1, oldCharacter, newCharacter) # down
	return world

def main():
	world = getWorldFromText()
	printWorld(world)
	print
	world = fillWorld(world, 5, 8, None, '+')
	printWorld(world)
	print
	world = fillWorld(world, 0, 0, None, 's')
	printWorld(world)
	print

if __name__ == '__main__':
	main()