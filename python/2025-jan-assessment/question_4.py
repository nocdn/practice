# simlified version of a game
# game consists of a set of tiles drawn from a bag each round by a player
# the player places the tile down against other placed tiles in such a way as to expand or create new features
# tiles can only be placed next to existing pieces and must extend the existing feature on all adjacent tiles
# tiles can be rotated to match the features of placed tiles
# tiles are randomly drawn from a bag and only a single tile is drawn by each player for their turn
# the first tile placed is considered the starting point for the game, with coords 0,0
# all other tiles are placed in relation to this tile
# tiles can have both positive and negative coords depending on where they are placed

# each tile has 4 sides, on each side there is a feature
# there can be different features on each side of a tile, or the same on all sides
# all sides must have a feature
# the features are as follows:
# C - City
# R - Road
# F - Field

import random

class GameTile:
    def __init__(self, features):
        if len(features) != 4:
            raise ValueError("Features must have exactly 4 items.")
        self._features = features
        self._coordinates = []
        self._orientation = 0

    @property
    def features(self):
        return self._features

    @property
    def orientation(self):
        return self._orientation

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coords):
        has_two_values = len(coords) == 2
        if not has_two_values:
            raise ValueError("Coordinates must have two values.")
        
        all_integers = all(isinstance(c, int) for c in coords)
        if not all_integers:
            raise TypeError("Coordinates must be integers.")
        
        self._coordinates = coords
    
    def __str__(self):
        if self._coordinates:
            x, y = self._coordinates
            coords_string = f"[{x},{y}]"
        else:
            coords_string = "none"
        
        features_string = ','.join(self._features)
        result = f"<{features_string},{coords_string},{self._orientation}>"
        return result
    
    def rotate(self, boolean):
        # a value of True means rotate clockwise by one position, False means rotate anti-clockwise by one position
        if boolean:
            self._orientation = (self._orientation + 1) % 4
        else:
            self._orientation = (self._orientation - 1) % 4

    def rotated_features(self):
        # Return features rotated based on current orientation
        rotation_amount = -self._orientation  # Negative because we rotate right
        return self._features[rotation_amount:] + self._features[:rotation_amount]


class BagOfTiles:
    def __init__(self):
        self._bag = []

    @property
    def bag(self):
        return self._bag

    def generate(self):
        # 6 tiles with same feature on all sides (2 each of [C,C,C,C], [R,R,R,R], [F,F,F,F])
        for features in (['C','C','C','C'], ['R','R','R','R'], ['F','F','F','F']):
            for _ in range(2):
                self._bag.append(GameTile(features))

        # 6 tiles with same feature on opposite sides (2 each of [C,R,C,R], [C,F,C,F], [R,F,R,F])
        for features in (['C','R','C','R'], ['C','F','C','F'], ['R','F','R','F']):
            for _ in range(2):
                self._bag.append(GameTile(features))

        # 6 tiles with same feature on adjacent sides (2 each of [C,C,R,R], [C,C,F,F], [R,R,F,F])
        for features in (['C','C','R','R'], ['C','C','F','F'], ['R','R','F','F']):
            for _ in range(2):
                self._bag.append(GameTile(features))

    def draw(self):
        if not self._bag:
            return None
        tile = random.choice(self._bag)
        self._bag.remove(tile)
        tile._orientation = random.randint(0, 3)
        return tile

    def isEmpty(self):
        return len(self._bag) == 0
    
class GameBoard:
    def __init__(self, start_tile):
        self._board = []
        self._available_spaces = []
        start_tile.coordinates = [0, 0]
        self._board.append(start_tile)
        self._update_spaces(start_tile)

    def _update_spaces(self, placed_tile):
        x, y = placed_tile.coordinates
        # remove the space from available_spaces (if present)
        if [x, y] in self._available_spaces:
            self._available_spaces.remove([x, y])
        # add adjacent coords if they are free
        for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if not any(t.coordinates == [nx, ny] for t in self._board):
                if [nx, ny] not in self._available_spaces:
                    self._available_spaces.append([nx, ny])

    def possible_moves(self, tile):
        valid_moves = []
        for space in self._available_spaces:
            x, y = space
            orientations = []
            # check all orientations 0..3
            for orientation in range(4):
                if self._is_valid_placement(tile, [x, y], orientation):
                    orientations.append(orientation)
            if orientations:
                valid_moves.append([x, y] + orientations)
        return valid_moves

    def _is_valid_placement(self, tile, coords, orientation):
        original_coords = tile.coordinates
        original_orientation = tile.orientation
        tile.coordinates = coords
        tile._orientation = orientation
        
        for board_tile in self._board:
            bx, by = board_tile.coordinates
            if [bx, by] in [(coords[0]+1, coords[1]),
                            (coords[0]-1, coords[1]),
                            (coords[0], coords[1]+1),
                            (coords[0], coords[1]-1)]:
                if not self._features_match(tile, board_tile):
                    tile.coordinates = original_coords
                    tile._orientation = original_orientation
                    return False
        
        tile.coordinates = original_coords
        tile._orientation = original_orientation
        return True

    def _features_match(self, new_tile, board_tile):
        nx, ny = new_tile.coordinates
        bx, by = board_tile.coordinates
        new_rot = new_tile.rotated_features()
        board_rot = board_tile.rotated_features()

        if bx == nx + 1 and by == ny:
            return new_rot[1] == board_rot[3]
        if bx == nx - 1 and by == ny:
            return new_rot[3] == board_rot[1]
        if bx == nx and by == ny + 1:
            return new_rot[0] == board_rot[2]
        if bx == nx and by == ny - 1:
            return new_rot[2] == board_rot[0]

        return True

    def place(self, tile, coords, orientation):
        if coords not in self._available_spaces:
            raise ValueError("Coordinates not available.")
        if not self._is_valid_placement(tile, coords, orientation):
            raise ValueError("Invalid placement.")
        
        tile.coordinates = coords
        tile._orientation = orientation
        self._board.append(tile)
        self._update_spaces(tile)

