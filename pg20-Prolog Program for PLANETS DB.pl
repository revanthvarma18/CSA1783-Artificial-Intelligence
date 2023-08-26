planet(mercury, 0.39, 0.06, inner).
planet(venus, 0.72, 0.82, inner).
planet(earth, 1, 1, inner).
planet(mars, 1.52, 0.11, inner).
planet(jupiter, 5.2, 317.8, outer).
planet(saturn, 9.58, 95.2, outer).
planet(uranus, 19.18, 14.6, outer).
planet(neptune, 30.07, 17.2, outer).

distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _, _).

planet_type(Planet, Type) :-
    planet(Planet, _, _, Type).

has_moon(Planet) :-
    planet(Planet, _, Moons, _),
    Moons > 0.
