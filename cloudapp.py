import json
import urllib2

class CloudApp(object):
    """
    API for ICFP 2013 cloudapp.net service.
    """

    API_KEY = "0127icY7OAJykdvpRzk7gE4pFJhYXlBV3AGnjKEvvpsH1H"

    def __init__(self):
        pass

    def _send_request(self, req_type, data):
        """
        Send a request to the service and get a response.

        Args:
            req_type: Type of request to send (train, eval, status, etc)
            data: Dictionary of data to send with request

        Returns:
            Dictionary of response from server.  In the format specified by
            the spec for the given request type.

        Raises:
            HTTPError if there is a problem with the request
        """
        req = urllib2.urlopen("http://icfpc2013.cloudapp.net/%s?auth=%s" % (req_type, self.API_KEY),
                              json.dumps(data))

        return json.loads(req.read())

    def problems(self):
        """
        Get new problem instance

        Returns:
            List of Problem dictionaries.  See spec.

        Raises:
            HTTPError if there is a problem with the request.
        """
        return self._send_request('myproblems', {})

    def eval(self, id=None, program=None, arguments=[]):
        """
        Evaluate a program.

        Evaluates either a string program that is provided, or a program from
        the server, specified by an id.

        id XOR program must be specified

        Args:
            id: ID of program to evaluate provided by server
            program: String program to evaluate
            argument: List of arguments to evaluate on

        Returns:
            EvalResponse dictionary.  See spec.

        Raises:
            AttributeError if id XOR program not specified.
            HTTPError if there is a problem with the request.
        """
        if (id and program) or (not id and not program):
            raise AttributeError("Either id or program must be specified")

        data = {'arguments': ["%#x" % n for n in arguments]}
        if id:
            data['id'] = id
        if program:
            data['program'] = program

        return self._send_request('eval', data)

    def guess(self, id, program):
        """
        Submit a guess for a program.

        Args:
            id: ID of program to submit guess for
            program: String program to guess

        Returns:
            GuessResponse dictionary.  See spec.

        Raises:
            HTTPError if there is a problem with the request.
        """
        data = {'id': id, 'program': program}

        return self._send_request('guess', data)

    def train(self, size, fold=None):
        """
        Get a training program

        Args:
            size: Size of the \BV program to return
            fold: Allow folds.  Either None, 'fold', or 'tfold'

        Returns:
            TrainingProblem dictionary.  See spec.

        Raises:
            HTTPError if there is a problem with the request.
        """
        data = { 'size': size, 'operators': [fold] if fold else [] }

        return self._send_request('train', data)

    def status(self):
        """
        Get team statistics

        Returns:
            Status dictionary.  See spec.

        Raises:
            HTTPError if there is a problem with the request.
        """
        return self._send_request('status', {})
