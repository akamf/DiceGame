def write_map(maze, out_file: str):
    """
    Write an map as an SVG (Scalable Vector Graphics) image of the map
    :param maze: Maze instance, the maze to write to SVG
    :param out_file: str, the file name for the output file
    :return None
    """

    def write_wall(wall_f, wall_x1, wall_y1, wall_x2, wall_y2):
        print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'
              .format(wall_x1, wall_y1, wall_x2, wall_y2), file=wall_f)

    aspect_ratio = maze.num_of_cells_x / maze.num_of_cells_y
    padding = 10
    height = 500
    width = int(height * aspect_ratio)  # Height and width of the map image in pixels
    scale_y, scale_x = height / maze.num_of_cells_y, width / maze.num_of_cells_x  # Scaling the map coordinates

    with open(out_file + '.svg', 'w') as f:
        # SVG preamble and styles.
        print('<?xml version="1.0" encoding="utf-8"?>', file=f)
        print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
        print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
        print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
              .format(width + 2 * padding, height + 2 * padding,
                      -padding, -padding, width + 2 * padding, height + 2 * padding),
              file=f)
        print('<defs>\n<style type="text/css"><![CDATA[', file=f)
        print('line {', file=f)
        print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
        print('    stroke-width: 5;\n}', file=f)
        print(']]></style>\n</defs>', file=f)
        # Draw the "South" and "East" walls of each cell,
        # these are the "North" and "West" walls of the neighbouring cell
        for x in range(maze.num_of_cells_x):
            for y in range(maze.num_of_cells_y):
                if maze.get_cell(x, y).walls['south']:
                    x1, y1, x2, y2 = x * scale_x, (y + 1) * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                    write_wall(f, x1, y1, x2, y2)
                if maze.get_cell(x, y).walls['east']:
                    x1, y1, x2, y2 = (x + 1) * scale_x, y * scale_y, (x + 1) * scale_x, (y + 1) * scale_y
                    write_wall(f, x1, y1, x2, y2)
        # Draw the North and West map border
        print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
        print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)
        print('</svg>', file=f)
