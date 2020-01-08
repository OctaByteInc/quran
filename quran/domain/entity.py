import dataclasses
from dataclasses import asdict


class Entity:

    @classmethod
    def from_dict(cls, a_dict):
        field_names = set(f.name for f in dataclasses.fields(cls))
        return cls(**{k:v for k,v in a_dict.items() if k in field_names})

    def to_dict(self):
        return asdict(self)