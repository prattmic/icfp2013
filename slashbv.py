import sexpdata

class SlashBV(object):
    """
    \BV language s-expression wrapper class

    Args:
        exp: String s-expression
    """

    def __init__(self, exp):
        self.expression = sexpdata.loads(exp)

    def __repr__(self):
        return "SlashBV('%s' -> %s)" % (self, str(self.expression))

    def __str__(self):
        return sexpdata.dumps(self.expression)

def magnitude(prog):
    """
    Compute the magnitude of an expression

    Based on the \BV spec, determine the magnitude of a given program

    Magnitude determined recursively

    Args:
        prog: Expression to determine magnitude of.  Either SlashBV object,
              or sexpdata expression list

    Returns:
        Magnitude of expression
    """
    if isinstance(prog, SlashBV):
        prog = prog.expression

    # Raw symbol
    if type(prog) != type([]):
        return 1

    # Empty set
    if not prog:
        return 0

    first = prog[0]
    if type(first) == type([]):
        # Extra (), unwrap them
        return magnitude(first) + magnitude(prog[1:])
    elif type(first) == sexpdata.Symbol:
        first = first.value()

    if first == 'lambda':
        # Cut off 'lamda' and arguemnt list
        return 1 + magnitude(prog[2:])

    # Cut off operator
    return 1 + magnitude(prog[1:])
