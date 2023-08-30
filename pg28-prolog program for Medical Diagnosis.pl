% Facts about illnesses and their symptoms
symptom(flu, fever).
symptom(flu, cough).
symptom(flu, sore_throat).
symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(headache, head_pain).

% Rule to diagnose illness based on symptoms
diagnose_illness(Symptoms, Illness) :-
    findall(I, (symptom(I, Sym), member(Sym, Symptoms)), PossibleIllnesses),
    list_to_set(PossibleIllnesses, UniqueIllnesses),
    length(UniqueIllnesses, NumUniqueIllnesses),
    NumUniqueIllnesses = 1,
    member(Illness, UniqueIllnesses).

% Main predicate to interact with the user
main :-
    write("Enter a list of symptoms (comma-separated): "),
    read(Symptoms),
    diagnose_illness(Symptoms, Illness),
    format("Based on the symptoms, the possible illness is: ~w", [Illness]).
