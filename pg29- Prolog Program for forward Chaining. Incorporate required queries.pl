% Define family relationships
parent(john, mary).
parent(john, alice).
parent(mary, jake).
parent(alice, bob).

% Define rules
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Forward chaining
:- dynamic known/2.

infer(KB) :-
    KB,
    (KB, !, fail ; true).

update_known(KB) :-
    KB,
    assertz(known(KB)).

start :-
    writeln("Inferred relationships:"),
    infer(ancestor(john, X)),
    known(ancestor(john, X)),
    writeln(X),
    fail.
start.

% Run the program
:- start.
