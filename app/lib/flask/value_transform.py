class ValueTransform:
    @staticmethod
    def intstr2int(int_string):
        if isinstance(int_string, str) and int_string.isdigit():
            int_string = int(int_string)
        return int_string

    @staticmethod
    def boolstr2bool(bool_string):
        return True if isinstance(bool_string, str) and bool_string.lower() == "true" else False


