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

; Test
(display (if0 0 0 1))
