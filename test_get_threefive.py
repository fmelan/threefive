from get_threefive import get_threefive


def test_get_threefive():

    nums = get_threefive(1, 100)

    assert nums
    assert len(nums) == 100
    assert nums[0] == 1
    assert nums[2] == "Three"
    assert nums[4] == "Five"
    assert nums[14] == "ThreeFive"
    assert nums[29] == "ThreeFive"
    assert nums[9] == "Five"
    assert nums[10] == 11