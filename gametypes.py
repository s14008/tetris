import pyglet
import random

class TetrominoType(object):
	def __init__(self, blockImage, localBlockCoordsByOrientation):
		self.blockImage = blockImage
		self.localBlockCoordsByOrientation = localBlockCoordsByOrientation

	@staticmethod
	def classInit(blocksImage, blockSize):
		green = blocksImage.get_region(x=0, y=0, width=blockSize, height=blockSize)
		blue = blocksImage.get_region(x=blockSize * 2.1, y=0, width=blockSize, height=blockSize)
		purple = blocksImage.get_region(x=blockSize * 5, y=0, width=blockSize, height=blockSize)
		orange = blocksImage.get_region(x=blockSize * 6.3, y=0, width=blockSize, height=blockSize)
		brown = blocksImage.get_region(x=blockSize * 8.43, y=0, width=blockSize, height=blockSize)
		red = blocksImage.get_region(x=blockSize * 10.53, y=0, width=blockSize, height=blockSize)
		yellow = blocksImage.get_region(x=blockSize * 12.57, y=0, width=blockSize, height=blockSize)

		TetrominoType.TYPES = [
   			TetrominoType(green,
    			{
	    			Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1), (3, 1)],
			    	Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (1, 3)],
			    	Tetromino.LEFT: [(0, 2), (1, 2), (2, 2), (3, 2)],
		    		Tetromino.UP: [(1, 0), (1, 1), (1, 2), (1, 3)]
    			}
			),
   			TetrominoType(blue,
    			{
	    			Tetromino.RIGHT: [(0, 0), (0, 1), (1, 0), (1, 1)],
	   	 			Tetromino.DOWN: [(0, 0), (0, 1), (1, 0), (1, 1)],
	    			Tetromino.LEFT: [(0, 0), (0, 1), (1, 0), (1, 1)],
	    			Tetromino.UP: [(0, 0), (0, 1), (1, 0), (1, 1)]
    			}
   			),
			TetrominoType(purple,
				{
					Tetromino.RIGHT: [(0, 1), (0, 2), (1, 0), (1, 1)],
					Tetromino.DOWN: [(0, 0), (1, 0), (1, 1), (2, 1)],
					Tetromino.LEFT: [(0, 1), (0, 2), (1, 0), (1, 1)],
					Tetromino.UP: [(0, 0), (1, 0), (1, 1), (2, 1)]
				}
			),
			TetrominoType(orange,
				{
					Tetromino.RIGHT: [(0, 1), (1, 1), (1, 2), (2, 1)],
					Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (2, 1)],
					Tetromino.LEFT: [(0, 1), (1, 0), (1, 1), (2, 1)],
					Tetromino.UP: [(0, 1), (1, 0), (1, 1), (1, 2)]
				}
			),
			TetrominoType(brown,
				{
					Tetromino.RIGHT: [(1, 0), (1, 1), (2, 1), (2, 2)],
					Tetromino.DOWN: [(0, 1), (1, 1), (1, 0), (2, 0)],
					Tetromino.LEFT: [(2, 2), (2, 1), (1, 1), (1, 0)],
					Tetromino.UP: [(2, 0), (1, 0), (1, 1), (0, 1)]

				}
			),
			TetrominoType(red,
				{
					Tetromino.RIGHT: [(0, 1), (0, 2), (1, 1), (2, 1)],
					Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (2, 2)],
					Tetromino.LEFT: [(0, 1), (1, 1), (2, 0), (2, 1)],
					Tetromino.UP: [(0, 0), (1, 0), (1, 1), (1, 2)]

				}
			),
			TetrominoType(yellow,
				{
					Tetromino.RIGHT: [(0, 1), (1, 1), (2, 1), (2, 2)],
					Tetromino.DOWN: [(1, 0), (1, 1), (1, 2), (2, 0)],
					Tetromino.LEFT: [(0, 0), (0, 1), (1, 1), (2, 1)],
					Tetromino.UP: [(0, 2), (1, 0), (1, 1), (1, 2)]
				}
			)

		]

	@staticmethod
	def randomType():
		return random.choice(TetrominoType.TYPES)

class Tetromino(object):
	RIGHT, DOWN, LEFT, UP = range(4)
	CLOCKWISE_ROTATIONS = {RIGHT: DOWN, DOWN: LEFT, LEFT: UP, UP: RIGHT}

	def __init__(self):
		self.x = 0
		self.y = 0
		self.tetrominoType = TetrominoType.randomType()
		self.orientation = Tetromino.RIGHT
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def calcBlockBoardCoords(self):
		localBlockCoords = self.tetrominoType.localBlockCoordsByOrientation[self.orientation]
		gridCoords = []
		for coord in localBlockCoords:
			gridCoord = (coord[0] + self.x, coord[1] + self.y)
			gridCoords.append(gridCoord)
		return gridCoords

	def setPosition(self, x, y):
		self.x = x
		self.y = y
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def moveDown(self):
		self.y -= 1
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def moveUp(self):
		self.y += 1
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def moveLeft(self):
		self.x -= 1
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def moveRight(self):
		self.x += 1
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def rotateClockwise(self):
		self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def rotateCounterclockwise(self):
		self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
		self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
		self.orientation = Tetromino.CLOCKWISE_ROTATIONS[self.orientation]
		self.blockBoardCoords = self.calcBlockBoardCoords()

	def command(self, command):
		if command == Input.MOVE_DOWN:
			self.moveDown()
		elif command == Input.MOVE_RIGHT:
			self.moveRight()
		elif command == Input.MOVE_LEFT:
			self.moveLeft()
		elif command == Input.ROTATE_CLOCKWISE:
			self.rotateClockwise()

	def undoCommand(self, command):
		if command == Input.MOVE_DOWN:
			self.moveUp()
		elif command == Input.MOVE_RIGHT:
			self.moveLeft()
		elif command == Input.MOVE_LEFT:
			self.moveRight()
		elif command == Input.ROTATE_CLOCKWISE:
			self.rotateCounterclockwise()

	def clearRowAndAdjustDown(self, boardGridRow):
		newBlockBoardCoords = []
		for coord in self.blockBoardCoords:
			if coord[1] > boardGridRow:
				adjustedCoord = (coord[0], coord[1] - 1)
				newBlockBoardCoords.append(adjustedCoord)
			if coord[1] < boardGridRow:
				newBlockBoardCoords.append(coord)
		self.blockBoardCoords = newBlockBoardCoords
		return len(self.blockBoardCoords) > 0

	def draw(self, screenCoords):
		image = self.tetrominoType.blockImage
		for coords in screenCoords:
			image.blit(coords[0], coords[1])


class Board(object):
	STARTING_ZONE_HEIGHT = 4
	NEXT_X = -5
	NEXT_Y = 20

	def __init__(self, x, y, gridWidth, gridHeight, blockSize):
		self.x = x
		self.y = y
		self.gridWidth = gridWidth
		self.gridHeight = gridHeight
		self.blockSize = blockSize
		self.spawnX = int(gridWidth * 1/3)
		self.spawnY = gridHeight
		self.nextTetromino = Tetromino()
		self.fallingTetromino = None
		self.spawnTetromino()
		self.tetrominos = []

	def spawnTetromino(self):
		self.fallingTetromino = self.nextTetromino
		self.nextTetromino = Tetromino()
		self.fallingTetromino.setPosition(self.spawnX, self.spawnY)
		self.nextTetromino.setPosition(Board.NEXT_X, Board.NEXT_Y)

	def commandFallingTetromino(self, command):
		self.fallingTetromino.command(command)
		if not self.isValidPosition():
			self.fallingTetromino.undoCommand(command)

	def isValidPosition(self):
		nonFallingBlockCoords = []
		for tetromino in self.tetrominos:
			nonFallingBlockCoords.extend(tetromino.blockBoardCoords)
		for coord in self.fallingTetromino.blockBoardCoords:
			outOfBounds = coord[0] < 0 or coord[0] >= self.gridWidth or coord[1] < 0
			overlapping = coord in nonFallingBlockCoords
			if outOfBounds or overlapping:
				return False
		return True

	def findFullRows(self):
		nonFallingBlockCoords = []
		for tetromino in self.tetrominos:
			nonFallingBlockCoords.extend(tetromino.blockBoardCoords)

		rowCounts = {}
		for i in range(self.gridHeight + Board.STARTING_ZONE_HEIGHT):
			rowCounts[i] = 0
		for coord in nonFallingBlockCoords:
			rowCounts[coord[1]] += 1

		fullRows = []
		for row in rowCounts:
			if rowCounts[row] == self.gridWidth:
				fullRows.append(row)
		return fullRows

	def clearRow(self, gridRow):
		tetrominos = []
		for tetromino in self.tetrominos:
			if tetromino.clearRowAndAdjustDown(gridRow):
				tetrominos.append(tetromino)
		self.tetrominos = tetrominos

	def clearRows(self, gridRows):
		gridRows.sort(reverse=True)
		for row in gridRows:
			self.clearRow(row)

	def updateTick(self):
		numClearedRows = 0
		gameLost = False
		self.fallingTetromino.command(Input.MOVE_DOWN)
		if not self.isValidPosition():
			self.fallingTetromino.undoCommand(Input.MOVE_DOWN)
			self.tetrominos.append(self.fallingTetromino)
			fullRows = self.findFullRows()
			self.clearRows(fullRows)
			gameLost = self.isInStartZone(self.fallingTetromino)
			if not gameLost:
				self.spawnTetromino()
			numClearedRows = len(fullRows)
		return (numClearedRows,  gameLost)

	def isInStartZone(self, tetromino):
		for coords in tetromino.blockBoardCoords:
			if coords[1] >= self.gridHeight:
				return True
		return False

	def gridCoordsToScreenCoords(self, coords):
		screenCoords = []
		for coord in coords:
			coord = (self.x + coord[0] * self.blockSize, self.y + coord[1] * self.blockSize)
			screenCoords.append(coord)
		return screenCoords

	def draw(self):
		for tetromino in self.tetrominos:
			screenCoords = self.gridCoordsToScreenCoords(tetromino.blockBoardCoords)
			tetromino.draw(screenCoords)

		screenCoords = self.gridCoordsToScreenCoords(self.fallingTetromino.blockBoardCoords)
		self.fallingTetromino.draw(screenCoords)

		screenCoords = self.gridCoordsToScreenCoords(self.nextTetromino.blockBoardCoords)
		self.nextTetromino.draw(screenCoords)

class InfoDisplay(object):
	ROWS_CLEARED_X = 70
	ROWS_CLEARED_Y = 550

	def __init__(self, window):
		self.rowsClearedLabel = pyglet.text.Label('Rows cleared: 0', font_size=14, x=InfoDisplay.ROWS_CLEARED_X, y=InfoDisplay.ROWS_CLEARED_Y)
		self.pausedLabel = pyglet.text.Label('PAUSED', font_size=32, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
		self.gameoverLabel = pyglet.text.Label('GAME OVER', font_size=32, x=window.width // 2, y=window.height // 2, anchor_x='center', anchor_y='center')
		self.showPausedLabel = False
		self.showGameoverLabel = False

	def setRowsCleared (self, numRowsCleared):
		self.rowsClearedLabel.text = 'Rows cleared: ' + str(numRowsCleared)

	def draw(self):
		self.rowsClearedLabel.draw()
		if self.showPausedLabel:
			self.pausedLabel.draw()
		if self.showGameoverLabel:
			self.gameoverLabel.draw()

class Input(object):
	TOGGLE_PAUSE, MOVE_DOWN, MOVE_LEFT, MOVE_RIGHT, ROTATE_CLOCKWISE = range(5)

	def __init__(self):
		self.action = None

	def processKeypress(self, symbol, modifiers):
		if symbol == pyglet.window.key.SPACE:
			self.action = Input.TOGGLE_PAUSE

	def processTextMotion(self, motion):
		if motion == pyglet.window.key.MOTION_LEFT:
			self.action = Input.MOVE_LEFT
		elif motion == pyglet.window.key.MOTION_RIGHT:
			self.action = Input.MOVE_RIGHT
		elif motion == pyglet.window.key.MOTION_UP:
			self.action = Input.ROTATE_CLOCKWISE
		elif motion == pyglet.window.key.MOTION_DOWN:
			self.action = Input.MOVE_DOWN

	def consume(self):
		action = self.action
		self.action = None
		return action

class GameTick(object):
	def __init__(self, tickOnFirstCall=False):
		self.tick = tickOnFirstCall
		self.started = tickOnFirstCall

	def isTick(self, nextTickTime):
		def setTick(dt):
			self.tick = True
		if not self.started:
			self.started = True
			pyglet.clock.schedule_once(setTick, nextTickTime)
			return False
		elif self.tick:
			self.tick = False
			pyglet.clock.schedule_once(setTick, nextTickTime)
			return True
		else:
			return False

class Game(object):
	def __init__(self, board, infoDisplay, input, backgroundImage):
		self.board = board
		self.infoDisplay = infoDisplay
		self.input = input
		self.backgroundImage = backgroundImage
		self.paused = False
		self.lost = False
		self.numRowsCleared = 0
		self.tickSpeed = 0.3
		self.ticker = GameTick()

	def addRowsCleared(self, rowsCleared):
		self.numRowsCleared += rowsCleared
		self.infoDisplay.setRowsCleared(self.numRowsCleared)

	def togglePause(self):
		self.paused = not self.paused
		self.infoDisplay.showPausedLabel = self.paused

	def update(self):
		if self.lost:
			self.infoDisplay.showGameoverLabel = True
		else:
			command = self.input.consume()
			if command == Input.TOGGLE_PAUSE:
				self.togglePause()
			if not self.paused:
				if command and command != Input.TOGGLE_PAUSE:
					self.board.commandFallingTetromino(command)
				if self.ticker.isTick(self.tickSpeed):
					self.rowsCleared, self.lost = self.board.updateTick()
					self.addRowsCleared(self.rowsCleared)

	def draw(self):
		self.backgroundImage.blit(0, 0)
		self.board.draw()
		self.infoDisplay.draw()

