class Field:
    field_index = 0

    # List to store all the connections with other fields
    connections = []

    # stores the piece, that lays on the board
    # 0 for none
    # 1 for white
    # 2 for black
    hold_piece = 0

    def __init__(self, field_index, empty_field):
        self.field_index = field_index
        self.hold_piece = empty_field

    def connect(self, field_to_connect):
        self.connections.append(field_to_connect)

    def change_hold_piece(self, new_piece):
        self.hold_piece = new_piece

    def hold_str(self):
        return str(self.hold_piece)
    