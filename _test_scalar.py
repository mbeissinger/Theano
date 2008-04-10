
import unittest

from gof import Result, Op, Env, modes
import gof

from scalar import *


def inputs():
    x = modes.build(as_scalar(1.0, 'x'))
    y = modes.build(as_scalar(2.0, 'y'))
    z = modes.build(as_scalar(3.0, 'z'))
    return x, y, z

def env(inputs, outputs, validate = True, features = []):
    return Env(inputs, outputs, features = features, consistency_check = validate)


class _test_ScalarOps(unittest.TestCase):

    def test_straightforward(self):
        x, y, z = inputs()
        e = mul(add(x, y), div(x, y))
        g = env([x, y], [e])
        fn = gof.DualLinker(g).make_function()
        assert fn(1.0, 2.0) == 1.5


if __name__ == '__main__':
    unittest.main()




