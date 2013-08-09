import json
import urllib2

class CloudApp(object):
    """
    API for ICFP 2013 cloudapp.net service.
    """

    API_KEY = "0127icY7OAJykdvpRzk7gE4pFJhYXlBV3AGnjKEvvpsH1H"

    def __init__(self):
        pass

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

        req = urllib2.urlopen("http://icfpc2013.cloudapp.net/train?auth=%s" % self.API_KEY,
                              json.dumps(data))

        return json.loads(req.read())
