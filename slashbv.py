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
