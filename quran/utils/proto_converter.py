class ProtoConverter:

    @classmethod
    def proto_to_dict(cls, proto_message):
        proto_dict = {}
        desc = proto_message.DESCRIPTOR

        for field in desc.fields:
            field_name = field.name
            proto_dict[field_name] = getattr(proto_message, field_name)

        return proto_dict