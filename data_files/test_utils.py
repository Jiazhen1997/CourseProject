from unittest import TestCase
import multiprocessing as mp
import random
import string

__author__ = 'Danyang'


class TestCounter(TestCase):
    def test_increment(self):
        pass

    def test_value(self):
        pass


def cube(x):
    
    return x**3


class TestMp(TestCase):
    
    def rand_string(self, length, output):
        
        rand_str = ''.join(random.choice(
            string.ascii_lowercase
            + string.ascii_uppercase
            + string.digits) for _ in range(length))

        output.put(rand_str)

    def test_generate_random_str(self):
        
        
        output = mp.Queue()

        
        processes = [mp.Process(target=self.rand_string, args=(5, output)) for x in range(4)]

        
        for p in processes:
            p.start()

        
        for p in processes:
            p.join()

        
        results = [output.get() for p in processes]

        self.assertEqual(len(results), 4)
        self.assertTrue(all(map(lambda x: len(x)==5, results)))

    def test_pool(self):
        
        expected = [1, 8, 27, 64, 125, 216]
        pool = mp.Pool(processes=4)
        results = [pool.apply(cube, args=(x,)) for x in range(1, 7)]
        self.assertEqual(results, expected)

        pool = mp.Pool(processes=4)
        results = pool.map(cube, range(1, 7))
        self.assertEqual(results, expected)

        pool = mp.Pool(processes=4)
        results = [pool.apply_async(cube, args=(x,)) for x in range(1, 7)]
        output = [p.get() for p in results]
        self.assertEqual(output, expected)