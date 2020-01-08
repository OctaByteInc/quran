from dataclasses import asdict


class Entity:

    @classmethod
    def from_dict(cls, a_dict):
        return cls(**a_dict)

    def to_dict(self):
        return asdict(self)