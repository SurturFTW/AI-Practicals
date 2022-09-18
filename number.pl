n_Range(0,0).
n_Range(H,L):-
between(H,L,M),
write(M).
