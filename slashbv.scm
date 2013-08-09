#lang scheme

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

; Test
(display ((lambda (x) (fold x 0 (lambda (x y) (plus x y)))) #x0201))
