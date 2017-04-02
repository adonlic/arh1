class CommandInstructionCondition:
    C = '_C'
    NC = '_NC'
    V = '_V'
    NV = '_NV'
    N = '_N'
    NN = '_NN'
    M = '_M'
    P = '_P'
    Z = '_Z'
    NZ = '_NZ'
    EQ = '_EQ'
    NE = '_NE'
    ULE = '_ULE'
    UGT = '_UGT'
    ULT = '_ULT'
    UGE = '_UGE'
    SLE = '_SLE'
    SGT = '_SGT'
    SLT = '_SLT'
    SGE = '_SGE'

    @staticmethod
    def all():
        return [CommandInstructionCondition.C, CommandInstructionCondition.NC,
                CommandInstructionCondition.V, CommandInstructionCondition.NV,
                CommandInstructionCondition.N, CommandInstructionCondition.NN,
                CommandInstructionCondition.M, CommandInstructionCondition.P,
                CommandInstructionCondition.Z, CommandInstructionCondition.NZ,
                CommandInstructionCondition.EQ, CommandInstructionCondition.NE,
                CommandInstructionCondition.ULE, CommandInstructionCondition.UGT,
                CommandInstructionCondition.ULT, CommandInstructionCondition.UGE,
                CommandInstructionCondition.SLE, CommandInstructionCondition.SGT,
                CommandInstructionCondition.SLT, CommandInstructionCondition.SGE]
