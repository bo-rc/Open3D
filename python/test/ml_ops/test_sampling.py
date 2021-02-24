# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# The MIT License (MIT)
#
# Copyright (c) 2020 www.open3d.org
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
# ----------------------------------------------------------------------------

import open3d as o3d
import numpy as np
import pytest
import mltest

# Skip all tests if the ml ops were not built.
pytestmark = mltest.default_marks


@mltest.parametrize.ml_gpu_only
def test_furthest_point_sampling(ml):

    values = mltest.fetch_numpy(
        'https://storage.googleapis.com/isl-datasets/open3d-dev/test/ml_ops/data/sampling/values.npy'
    )
    samples = 4096

    ans = mltest.run_op(ml, ml.device, True, ml.ops.furthest_point_sampling,
                        values, samples)

    expected = mltest.fetch_numpy(
        'https://storage.googleapis.com/isl-datasets/open3d-dev/test/ml_ops/data/sampling/out.npy'
    )
    np.testing.assert_equal(ans, expected)
