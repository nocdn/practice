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
        return f"<{features_string},{coords_string},{self._orientation}>"

    def rotate(self, boolean):
        if boolean:
            self._orientation = (self._orientation + 1) % 4
        else:
            self._orientation = (self._orientation - 1) % 4

    def rotated_features(self):
        rotation_amount = -self._orientation
        return self._features[rotation_amount:] + self._features[:rotation_amount]


class BagOfTiles:
    def __init__(self):
        self._bag = []

    @property
    def bag(self):
        return self._bag

    def generate(self):
        for features in (['C','C','C','C'], ['R','R','R','R'], ['F','F','F','F']):
            for _ in range(2):
                self._bag.append(GameTile(features))
        for features in (['C','R','C','R'], ['C','F','C','F'], ['R','F','R','F']):
            for _ in range(2):
                self._bag.append(GameTile(features))
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
        if [x, y] in self._available_spaces:
            self._available_spaces.remove([x, y])
        for nx, ny in [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]:
            if not any(t.coordinates == [nx, ny] for t in self._board):
                if [nx, ny] not in self._available_spaces:
                    self._available_spaces.append([nx, ny])

    def _features_match(self, new_tile, board_tile):
        nx, ny = new_tile.coordinates
        bx, by = board_tile.coordinates
        new_rot = new_tile.rotated_features()
        board_rot = board_tile.rotated_features()
    
        # Check all adjacent connections
        if bx == nx + 1 and by == ny:  # board tile is to the right
            return new_rot[1] == board_rot[3]
        if bx == nx - 1 and by == ny:  # board tile is to the left
           return new_rot[3] == board_rot[1]
        if by == ny + 1 and bx == nx:  # board tile is above
            return new_rot[0] == board_rot[2]
        if by == ny - 1 and bx == nx:  # board tile is below
            return new_rot[2] == board_rot[0]
        return True

    def _restore_state(self, tile, old_coords, old_orientation):
        # Restore orientation first
        tile._orientation = old_orientation
        # If old_coords had 2 values, restore via the property setter.
        # Otherwise, restore directly so we don't trigger a ValueError.
        if len(old_coords) == 2:
            tile.coordinates = old_coords
        else:
            tile._coordinates = old_coords

    def _is_valid_placement(self, tile, coords, orientation):
        has_adjacent = False
        original_coords = tile._coordinates[:]
        original_orientation = tile._orientation
    
        # Set temporary state
        tile._coordinates = coords
        tile._orientation = orientation
    
        # Check all adjacent tiles
        for board_tile in self._board:
            bx, by = board_tile.coordinates
            if [bx, by] in [
                [coords[0]+1, coords[1]],
                [coords[0]-1, coords[1]],
                [coords[0], coords[1]+1],
                [coords[0], coords[1]-1]
            ]:
                has_adjacent = True
                if not self._features_match(tile, board_tile):
                    # Restore original state
                    tile._coordinates = original_coords
                    tile._orientation = original_orientation
                    return False
    
        # Restore original state
        tile._coordinates = original_coords
        tile._orientation = original_orientation
        return has_adjacent or len(self._board) == 0


    def possible_moves(self, tile):
        moves_dict = {}  # Group orientations by coordinate
        original_coords = tile.coordinates
        original_orientation = tile.orientation
        
        for space in self._available_spaces:
            valid_orientations = []
            for orientation in range(4):
                if self._is_valid_placement(tile, space, orientation):
                    valid_orientations.append(orientation)
            if valid_orientations:
                moves_dict[tuple(space)] = valid_orientations
        
        # Restore original state
        if len(original_coords) == 2:
            tile.coordinates = original_coords
        else:
            tile._coordinates = []
        tile._orientation = original_orientation
        
        # Format moves as required: [[x,y,orientation1,orientation2,...],...]
        valid_moves = []
        for coord, orientations in moves_dict.items():
            move = [coord[0], coord[1]] + orientations
            valid_moves.append(move)
        
        return valid_moves

    def place(self, tile, coords, orientation):
        if not isinstance(coords, list) or len(coords) != 2:
            raise ValueError("Coordinates must be a list of two values.")
        if coords not in self._available_spaces:
            raise ValueError("Coordinates not available.")
        if not self._is_valid_placement(tile, coords, orientation):
            raise ValueError("Invalid placement.")
    
        # Update tile state
        tile._coordinates = coords
        tile._orientation = orientation
        self._board.append(tile)
        self._update_spaces(tile)