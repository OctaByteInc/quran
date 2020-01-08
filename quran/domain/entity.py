
class Entity:

    @classmethod
    def from_dict(cls, a_dict):
        return cls(**a_dict)