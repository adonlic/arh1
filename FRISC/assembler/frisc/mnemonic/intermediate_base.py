class IntermediateBase:
    B = '%B'    # binary format
    D = '%D'    # usual numbers human use everyday
    H = '%H'    # hexadecimal format

    @staticmethod
    def all():
        return [IntermediateBase.B, IntermediateBase.D, IntermediateBase.H]
