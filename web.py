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
