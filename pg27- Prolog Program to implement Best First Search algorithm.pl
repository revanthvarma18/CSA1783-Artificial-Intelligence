% Sample graph represented as facts and rules
edge(a, b, 4).
edge(a, c, 2).
edge(b, d, 5).
edge(c, d, 1).
edge(c, e, 3).
edge(d, e, 8).
edge(d, f, 10).
edge(e, f, 2).

% Heuristic function: estimated cost from a node to the goal
heuristic(Node, HeuristicValue) :-
    goal(Goal),
    distance(Node, Goal, HeuristicValue).

% Helper predicate to calculate distance between two nodes
distance(Node1, Node2, Distance) :-
    edge(Node1, Node2, Distance).
distance(Node1, Node2, Distance) :-
    edge(Node2, Node1, Distance).

% Best First Search algorithm
best_first_search(Node, Path) :-
    goal(Goal),
    best_first_search_helper([[(Node, 0, 0)]], Goal, [], Path).

% Base case: Goal node is reached
best_first_search_helper([[Node | Path] | _], Node, Path, [Node | Path]).

% Recursive case: Expand the best node and continue the search
best_first_search_helper([[Node | Path] | RestPaths], Goal, Visited, FinalPath) :-
    expand(Node, Path, Expansions),
    append(Expansions, RestPaths, NewPaths),
    select_best(NewPaths, SelectedPath),
    best_first_search_helper(SelectedPath, Goal, [Node | Visited], FinalPath).

% Expand a node to its neighbors
expand(Node, Path, Expansions) :-
    findall([Neighbor, Node | Path],
            (edge(Node, Neighbor, _), \+ member(Neighbor, Path)),
            Expansions).

% Select the best path based on heuristic value
select_best(Paths, BestPath) :-
    map_list_to_pairs(heuristic, Paths, PathsWithHeuristics),
    keysort(PathsWithHeuristics, Sorted),
    pairs_values(Sorted, SortedPaths),
    member(BestPath, SortedPaths).

% Example usage
goal(f). % Define the goal node

?- best_first_search(a, Path).
