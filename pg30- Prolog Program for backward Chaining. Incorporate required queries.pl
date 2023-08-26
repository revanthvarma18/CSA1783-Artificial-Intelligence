% Define the clues and relationships
owns(john, cat).
owns(susan, dog).
owns(mary, parrot).

friend(john, susan).
friend(susan, mary).

% Backward chaining
owns_pet(X, Pet) :-
    owns(X, Pet).

owns_pet(X, Pet) :-
    friend(X, Y),
    owns_pet(Y, Pet).

% Run the program
:- writeln("People and their pets:"),
   owns_pet(john, Pet),
   writeln("John owns a " + Pet + "."),
   fail.

:- owns_pet(susan, Pet),
   writeln("Susan owns a " + Pet + "."),
   fail.

:- owns_pet(mary, Pet),
   writeln("Mary owns a " + Pet + "."),
   fail.
