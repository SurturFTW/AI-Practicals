n_range(0,0).

n_range(H,L):-
    between(H,L,M),
    write(M).