#lang scheme

; Stupid Scheme
(define (uint64 x)
 (bitwise-and #xFFFFFFFFFFFFFFFF x))

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

; Test
(display (shr4 #xfffff))
