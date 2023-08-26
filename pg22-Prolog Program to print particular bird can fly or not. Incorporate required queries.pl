bird(eagle, can_fly).
bird(penguin, cannot_fly).
bird(ostrich, cannot_fly).
bird(sparrow, can_fly).

can_fly(Bird) :- bird(Bird, can_fly).
cannot_fly(Bird) :- bird(Bird, cannot_fly).
