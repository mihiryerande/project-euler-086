# Problem 86:
#     Cuboid Route
#
# Description:
#     A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3,
#       and a fly, F, sits in the opposite corner.
#     By travelling on the surfaces of the room the shortest "straight line" distance
#       from S to F is 10 and the path is shown on the diagram.
#
#         [ No Diagram, sorry ]
#
#     However, there are up to three "shortest" path candidates for any given cuboid
#       and the shortest route doesn't always have integer length.
#     It can be shown that there are exactly 2060 distinct cuboids,
#       ignoring rotations, with integer dimensions,
#       up to a maximum size of M by M by M,
#       for which the shortest route has integer length when M = 100.
#     This is the least value of M for which the number of solutions first exceeds two thousand;
#       the number of solutions when M = 99 is 1975.
#
#     Find the least value of M such that the number of solutions first exceeds one million.

from math import sqrt
from typing import Tuple

################################################################################
################################## UNFINISHED ##################################
################################################################################


def is_square(x: int) -> bool:
    """
    Returns True iff `x` is a square number.

    Args:
        x (int): Integer

    Returns:
        (bool): True iff `x` is square
    """
    if x < 0:
        return False
    else:
        s = sqrt(x)
        return int(s) == s


def main(n: int) -> Tuple[int, int]:
    """
    Returns the least value of `M` such that among cuboids having any max dimension M,
      there are over `n` such distinct cuboids having an integral shortest path between opposite corners.

    Args:
        n (int): Natural number

    Returns:
        (Tuple[int, int]):
            Tuple of ...
              * Least maximum cuboid dimension `M` s.t. number of integral shortest paths exceeds `n`
              * Number of distinct cuboid solutions for that value of `M`

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(n) == int and n > 0

    # UNFINISHED:
    #
    #     Try generating Pythagorean triples using Euclid's formula.
    #     Then deconstruct those into cuboid dimensions.
    #     Answer should be (1818, 1000457)

    # Idea 1:
    #     Suppose we have a cuboid of dimensions `x` by `y` by `z`.
    #     Assume (without loss of generality) that x <= y <= z.
    #
    #     As mentioned in the problem statement, there is a spider at one corner (S),
    #       and a fly at the opposite corner (F).
    #     We are interested in the shortest path from S -> F, by walking only on the faces of the cuboid.
    #     How can we get from S to F?
    #
    #     In order to go directly from S to F, we must traverse two faces.
    #     Imagine 'unfolding' two adjacent faces to form a single rectangle, as seen here:
    #
    #             ┌─────┐(F)       ┌─────┐(F)
    #             │     │          │     │x
    #             ├─────┤   --->   ├─────┤
    #            ╱     ╱           │     │y
    #         (S)‾‾‾‾‾          (S)└──z──┘
    #
    #     The direct path from S to F, using these two faces, is thus the diagonal across the unfolded 2-face.
    #     Using the Pythagorean theorem, the length of the direct path is sqrt( (x+y)^2 + z^2 ).

    # Idea 2:
    #     Building on the previous Idea #1, there are various candidates for direct path from S to F.
    #     Which of these is the shortest?
    #
    #     First, there are 3 faces which connect to S.
    #     From each of the 3 faces, there are 2 adjacent faces which extend to connect S to F.
    #     This gives 6 candidates for shortest paths.
    #
    #     Doing the same 'unfolding' as in Idea #1, we obtain 3 distinct unfolded 2-face rectangle dimensions:
    #         (x + y) by z
    #         (x + z) by y
    #         (y + z) by x
    #
    #     The direct path lengths by traversing each 2-face are thus the following:
    #         sqrt( (x + y)^2 + z^2 )
    #         sqrt( (x + z)^2 + y^2 )
    #         sqrt( (y + z)^2 + x^2 )
    #
    #     Ignore the radicals and simply compare the radicands.
    #         (x + y)^2 + z^2
    #         (x + z)^2 + y^2
    #         (y + z)^2 + x^2
    #
    #     Expanding these, we obtain the following:
    #         x^2 + 2xy + y^2 + z^2     = x^2 + y^2 + z^2 + 2xy
    #         x^2 + 2xz + z^2 + y^2     = x^2 + y^2 + z^2 + 2xz
    #         y^2 + 2yz + z^2 + x^2     = x^2 + y^2 + z^2 + 2yz
    #
    #     Now we are simply comparing the pairwise products of {x,y,z}, which are {xy,xz,yz}.
    #
    #     Recall that x <= y <= z (by assumption, without loss of generality).
    #     Thus we know the following:
    #         x <= z    ->  xy <= yz
    #         y <= z    ->  xy <= xz
    #
    #     So xy is the least of the pairwise products.
    #     The 2-face corresponding to this is the unfolded rectangle of dimensions (x+y) and z.
    #
    #     We conclude that if we have a cuboid
    #       having longest dimension is `z`
    #       and lesser dimensions are `x` and `y`,
    #       the shortest distance between opposite corners is:
    #         sqrt( (x+y)^2 + z^2 )

    # Idea 3:
    #     From Idea #2, we have a formula for shortest path.
    #     The shortest path is integral iff the radicand is square.

    # Idea 4:
    #     We are considering all distinct cuboids of integral dimensions.
    #     Cuboids that are rotationally equal should not be considered distinct,
    #       for example 3 x 5 x 6 is the same as 6 x 3 x 5.
    #     To avoid redundancy, we can simply consider a cuboid by its ordered dimensions,
    #       meaning 3 x 5 x 6 only, in the example.
    #
    #     This is not difficult for iteration, as we simply choose {x,y,z} such that the ordering constraint is met.

    # Idea 5:
    #     Suppose we have already considered cuboids having maximum dimension `M`.
    #     Now we would like to consider those for `M+1` which have not already been checked.
    #     This set (Cuboids[M+1] \ Cuboids[M]) includes cuboids having at least one dimension equalling `M+1`.
    #
    #     We can thus iterate through the cuboids in this incremental set
    #       by fixing the longest side length `z` as `M+1`.
    #     Then `x` and `y` can be anything up to and including `M+1`,
    #       still maintaining the ordering constraint from Idea #4

    count = 0
    m = 0

    while count <= n:
        # Try next incremental set of cuboids
        m += 1

        # Count up additional cuboids having integral shortest path distance from S to F
        z = m
        for x in range(1, m+1):  # `x` is least dimension
            for y in range(x, m+1):  # `x` <= `y`
                if is_square((x+y)**2 + z**2):
                    count += 1

        print('M = {}\t -> {}'.format(m, count))

    # Loop broke, so count > n
    return m, count


if __name__ == '__main__':
    solution_count = int(input('Enter a natural number: '))
    dimension_max, dimension_solutions = main(solution_count)
    print('Cuboid dimension `M` first having over {} integral shortest paths:'.format(solution_count))
    print('  M     = {}'.format(dimension_max))
    print('  Count = {}'.format(dimension_solutions))
