ICFP 2013
========

slashbv.scm is a Racket file that implements the \BV language.  It takes a string \BV program as the first arguement, and a list of inputs to evaluate following.  It outputs a list of the results.  It can be run like so:

    $ racket -tm- slashbv.scm "(lambda (x) (fold x 0 (lambda (x y) (plus x y))))" 512 513 514
    (2 3 4)

See http://stackoverflow.com/a/6380648/10817 for info on the Racket arguments.
