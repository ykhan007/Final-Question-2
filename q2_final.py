def make_base_grid(size, stop):
    """Build TL-based grid where each diagonal r+c has same value."""
    grid = []
    for r in range(size):
        row = []
        for c in range(size):
            val = r + c + 1          # diagonal index + 1
            if val <= stop:
                row.append(val)
            else:
                row.append(0)
        grid.append(row)
    return grid


def orient_grid(grid, corner):
    """Flip the base grid to match the chosen corner."""
    corner = corner.upper()
    n = len(grid)

    # start from a copy so we don't mutate original
    g = [row[:] for row in grid]

    if corner == "TL":
        # no change
        return g

    if corner == "BL":
        # flip vertically
        g.reverse()
        return g

    if corner == "TR":
        # flip horizontally
        return [list(reversed(row)) for row in g]

    if corner == "BR":
        # flip vertically then horizontally
        g.reverse()
        return [list(reversed(row)) for row in g]

    # if somehow invalid, just return as-is
    return g


def main():
    size = int(input("Enter grid size (1–8): "))
    corner = input("Choose starting corner: TL, TR, BL, BR\nCorner: ").strip()
    stop = int(input("Enter stop number: "))

    base = make_base_grid(size, stop)
    grid = orient_grid(base, corner)

    for row in grid:
        print(row)


if __name__ == "__main__":
    main()
