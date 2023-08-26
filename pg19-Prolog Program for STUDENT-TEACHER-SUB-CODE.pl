student(john, [math, science, history]).
student(susan, [english, art]).
student(jim, [math, science, art]).

teacher(ms_johnson, math).
teacher(mr_lee, science).
teacher(mrs_doe, history).
teacher(ms_jones, english).
teacher(mr_lewis, art).

student_teacher(S, T) :-
    student(S, Subjects),
    member(Subject, Subjects),
    teacher(T, Subject).    
