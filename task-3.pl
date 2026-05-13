% --- Facts ---
parent(kamau, wanjiru).
parent(kamau, otieno).
parent(wanjiru, edah).
parent(wanjiru, brian).
parent(otieno, mercy).
parent(otieno, daniel).

male(kamau).
male(otieno).
male(brian).
male(daniel).

female(wanjiru).
female(edah).
female(mercy).

% --- Rules ---
child(X, Y) :- parent(Y, X).

grandparent(X, Y) :- parent(X, Z), parent(Z, Y).

grandchild(X, Y) :- grandparent(Y, X).

sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.

cousin(X, Y) :- parent(P1, X), parent(P2, Y), sibling(P1, P2).

uncle(X, Y) :- male(X), sibling(X, P), parent(P, Y).

aunt(X, Y) :- female(X), sibling(X, P), parent(P, Y).