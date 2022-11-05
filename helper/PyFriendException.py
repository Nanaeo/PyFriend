print("om")
class PyFriendException(Exception):
    def __init__(self, Type,Location,Msg,Color = 0):
        self.Type = Type
        self.Location = Location
        self.Msg = Msg
        self.Color = Color
