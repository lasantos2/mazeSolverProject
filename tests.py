import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0,0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12

        m1 = Maze(0,0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )

        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10

        m1 = Maze(0,0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_rows-1].has_bottom_wall,
            False
        )

    def test_maze_break_walls_next_to_each_other(self):
        num_cols = 3
        num_rows = 1

        m1 = Maze(0,0, num_rows, num_cols, 10, 10)

        m1._break_walls_r(0,0)

        self.assertEqual(
            m1._cells[0][0].has_right_wall,
            False
        )

    def test_maze_break_walls_below_to_each_other(self):
        num_cols = 1
        num_rows = 3

        m1 = Maze(0,0, num_rows, num_cols, 10, 10)

        m1._break_walls_r(0,0)

        self.assertEqual(
            m1._cells[0][2]._visited,
            True
        )

    
    def test_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5

        m1 = Maze(0,0, num_rows, num_cols, 10, 10, None, 0)

        m1._break_walls_r(0,0)

        m1._reset_cells_visited()


        for i in m1._cells:
            for j in i:
                self.assertEqual(
                    j._visited,
                    False
                )



if __name__ == "__main__":
    unittest.main()

