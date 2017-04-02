import sys
import os
from datetime import datetime
from time import time

from FRISC.assembler.assembler import FRISCAssembler
from FRISC.shared.alu import FRISCArithmeticLogicInstruction


if __name__ == '__main__':
    # alu = FRISCArithmeticLogicInstruction()
    code = FRISCArithmeticLogicInstruction.Builder.getInstance().generate_machine_code('OR', 'r5', 'r6', 'r7')
    # code = alu.instr_or('r5', 'r6', 'r7')

    # input_rows = sys.stdin.readlines()
    # input_rows = open('TEST_EXAMPLES/test1.a', 'r')
    input_rows = open('TEST_EXAMPLES/test1.a', 'r').readlines()

    start_time = time()
    assembler = FRISCAssembler.getInstance()
    elapsed_time = start_time - time()

    if not assembler.assemble(input_rows):
        sys.stdout.write(assembler.getMessages().getErrorsPrintableRepr())
    else:
        # lexical_analysis_output = open('OUTPUT/bla.b', 'w')
        # *.lex file would be good :P
        lexical_analysis_output = open(
            '_RESULT_REPORTS/' + os.path.splitext(os.path.basename('TEST_EXAMPLES/test1.a'))[0] + '_lex.txt', 'w')
        lexical_analysis_output.write(
            'Generated:\t\t\t{}\nAssembling time\t\t= {} seconds\n\n'
                .format(datetime.now().strftime('%d-%m-%Y %H:%M:%S'), elapsed_time))
        lexical_analysis_output.write(assembler.getLexicalAnalysisReport())
        lexical_analysis_output.close()

    # if assembler.getMachineCode() is not None:
    #     sys.stdout.write(FRISCAssembler)
    # else:
    #     sys.stdout.write('NO OUTPUT')
