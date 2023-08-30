% Facts representing parent-child relationships
parent(john, mary).
parent(john, alice).
parent(alice, bob).
parent(alice, carol).
parent(mary, david).
parent(mary, emma).
parent(david, frank).
parent(david, grace).

% Rules for defining different relationships
sibling(X, Y) :-
    parent(P, X),
    parent(P, Y),
    X \= Y.

grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).

ancestor(X, Z) :-
    parent(X, Z).
ancestor(X, Z) :-
    parent(X, Y),
    ancestor(Y, Z).
