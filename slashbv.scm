#lang racket/base

(require racket/string)
(require racket/list)
(provide main)

; Create \BV namespace
(define-namespace-anchor bv)
(define ns (namespace-anchor->namespace bv))

; Stupid Scheme
(define (uint64 x)
 (bitwise-and #xFFFFFFFFFFFFFFFF x))

; List all bytes in a uint64
(define (byte-list x)
 (list
  (arithmetic-shift (bitwise-and x #xff) 0)
  (arithmetic-shift (bitwise-and x #xff00) -8)
  (arithmetic-shift (bitwise-and x #xff0000) -16)
  (arithmetic-shift (bitwise-and x #xff000000) -24)
  (arithmetic-shift (bitwise-and x #xff00000000) -32)
  (arithmetic-shift (bitwise-and x #xff0000000000) -40)
  (arithmetic-shift (bitwise-and x #xff000000000000) -48)
  (arithmetic-shift (bitwise-and x #xff00000000000000) -56)))

(define (not x)
 (uint64 (bitwise-not (uint64 x))))

(define (shl1 x)
 (uint64 (arithmetic-shift (uint64 x) 1)))

(define (shr1 x)
 (uint64 (arithmetic-shift (uint64 x) -1)))

(define (shr4 x)
 (uint64 (arithmetic-shift (uint64 x) -4)))

(define (shr16 x)
 (uint64 (arithmetic-shift (uint64 x) -16)))

(define (and x y)
 (bitwise-and (uint64 x) (uint64 y)))

(define (or x y)
 (bitwise-ior (uint64 x) (uint64 y)))

(define (xor x y)
 (bitwise-xor (uint64 x) (uint64 y)))

(define (plus x y)
 (uint64 (+ (uint64 x) (uint64 y))))

(define (if0 t x y)
 (if (= t 0) x y))

(define (fold x init op)
 (foldl op init (byte-list (uint64 x))))

; Take string program as first argument, test cases as remaining arguments
(define (main . xs)
 ; Some magic to turn the string program into something that can be eval'd
 ; It is eval'd into a procedure that can be run
 ; It is eval'd in namespace 'ns', which contains everything in this file
 (define prog (eval (read (open-input-string (first xs))) ns))
 ; Map the rest of the arguements to numbers
 (define inputs (map string->number (rest xs)))
 ; Map the inputs to outputs of the program, display them
 (display (map prog inputs)))
