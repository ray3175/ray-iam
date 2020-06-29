class ValueTransform:
    @staticmethod
    def intstr2int(int_string):
        return int(int_string) if (isinstance(int_string, str) and int_string.isdigit()) or isinstance(int_string, (int, float)) else None

    @staticmethod
    def floatstr2float(float_string):
        return float(float_string) if (isinstance(float_string, str) and all([int_string.isdigit() for int_string in float_string.split(".")])) or isinstance(float_string, (int, float)) else None

    @staticmethod
    def boolstr2bool(bool_string):
        if isinstance(bool_string, str):
            if bool_string.lower() == "true":
                return True
            elif bool_string.lower() == "false":
                return False
        return None


