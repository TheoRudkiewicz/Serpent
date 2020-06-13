from unittest import main, TestCase
from formules_3xn_clean_pre_pb_pa import parcours_3xn
from matrice_parcour_sans_try_numba_bord import count_path as count_path
# from parcour_to_go import count_path as count_path


class TestParcourBrut(TestCase):
    def setUp(self):
        self.pa2 = lambda n: 2 * (n ** 2 - n + 2)

    def test_2_n_soft(self):
        for n in range(2, 15):
            self.assertEqual(count_path(2, n), self.pa2(n))

    def test_n_2_soft(self):
        for n in range(2, 15):
            self.assertEqual(count_path(n, 2), self.pa2(n))

    def test_3_n_soft(self):
        for n in range(2, 11):
            self.assertEqual(count_path(3, n), parcours_3xn(n))

    def test_n_3_soft(self):
        for n in range(2, 11):
            self.assertEqual(count_path(n, 3), parcours_3xn(n))

    def test_soft(self):
        self.assertEqual(count_path(4, 4), 552)
        self.assertEqual(count_path(5, 5), 8648)

    """def test_2_n_hard(self):
            for n in range(15, 25):
                self.assertEqual(count_path(2, n), self.pa2(n))

    def test_2_n_hard(self):
            for n in range(15, 25):
                self.assertEqual(count_path(n, 2), self.pa2(n))

    def test_3_n_hard(self):
            for n in range(11, 15):
                self.assertEqual(count_path(3, n), parcours_3xn(n))

    def test_n_3_hard(self):
            for n in range(11, 15):
                self.assertEqual(count_path(n, 3), parcours_3xn(n))

    def test_hard(self):
        self.assertEqual(count_path(6, 6), 458_696)"""


if __name__ == '__main__':
    main()
