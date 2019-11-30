class ValueTransform:
    @classmethod
    def intstr2int(cls, int_string):
        if isinstance(int_string, str) and int_string.isdigit():
            int_string = int(int_string)
        return int_string

    @classmethod
    def boolstr2bool(cls, bool_string):
        return True if isinstance(bool_string, str) and bool_string.lower() == "true" else False


