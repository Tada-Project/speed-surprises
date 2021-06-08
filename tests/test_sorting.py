"""Tests for the Sorting function in the Sorting module of the lists package."""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import integers
from hypothesis.strategies import lists

from speedsurprises.lists import sorting


@pytest.mark.benchmark
def test_insertionSort_benchmark(benchmark):
    """Benchmark the insertionSort function."""
    sorted_list = benchmark(sorting.insertion_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(listInput=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_insertionSort_hypothesis(listInput):
    """Using hypothesis to ensure that insertion_sort works like built-in sorting function."""
    insertionSort_list = sorting.insertion_sort(listInput)
    python_sort_list = sorted(listInput)
    assert insertionSort_list == python_sort_list


@pytest.mark.parametrize(
    "list_input, expected_answer",
    [([6, 4, 8, 3, 2], [2, 3, 4, 6, 8]), ([3, 2, 1, 4], [1, 2, 3, 4])],
)
def test_insertionSort_multiple(list_input, expected_answer):
    """Check the insertionSort function with multiple lists."""
    sorted_list = sorting.insertion_sort(list_input)
    assert sorted_list == expected_answer


def test_insertionSort_single():
    """Check the insertionSort function with a single list."""
    sorted_list = sorting.insertion_sort([4, 3, 1, 5, 6])
    assert sorted_list == [1, 3, 4, 5, 6]


@pytest.mark.benchmark
def test_bubble_sort_benchmark(benchmark):
    """Benchmark the bubble_sort function."""
    sorted_list = benchmark(sorting.bubble_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_bubble_sort_hypothesis_integer_lists_yes(list_inputs):
    """Ensure list of hypothesis-generated data using bubble_sort is equal to data sort function."""
    bubble_sort_list = sorting.bubble_sort(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert bubble_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_bubble_sort_multiple(list_inputs, expected_answer):
    """Check the bubble_sort function with multiple inputs."""
    sorted_list = sorting.bubble_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([10, 3, 1], [1, 3, 10])],
)
def test_bubble_sort_single(list_inputs, expected_answer):
    """Check the bubble_sort function with one input."""
    sorted_list = sorting.bubble_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_merge_sort_benchmark(benchmark):
    """Benchmark the merge_sort function."""
    sorted_list = benchmark(sorting.merge_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_merge_sort_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted using merge_sort equal sorted using sort."""
    merge_sort_list = sorting.merge_sort(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert merge_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_merge_sort_multiple(list_inputs, expected_answer):
    """Check the merge_sort function with multiple inputs."""
    sorted_list = sorting.merge_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([10, 3, 1], [1, 3, 10])],
)
def test_merge_sort_single(list_inputs, expected_answer):
    """Check the merge_sort function with one input."""
    sorted_list = sorting.merge_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_tim_sort_v1_benchmark(benchmark):
    """Benchmark the tim_sort_v1 function."""
    sorted_list = benchmark(sorting.tim_sort_v1, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_tim_sort_v1_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted using tim_sort_v1 equal to data Python's."""
    tim_sort_list = sorting.tim_sort_v1(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert tim_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_tim_sort_v1_multiple(list_inputs, expected_answer):
    """Check the tim_sort_v1 function with multiple inputs."""
    sorted_list = sorting.tim_sort_v1(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([10, 3, 1], [1, 3, 10])],
)
def test_tim_sort_v1_single(list_inputs, expected_answer):
    """Check the tim_sort_v1 function with one input."""
    sorted_list = sorting.tim_sort_v1(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_tim_sort_v2_benchmark(benchmark):
    """Benchmark the tim_sort_v1 function."""
    sorted_list = benchmark(sorting.tim_sort_v2, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_tim_sort_v2_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted using tim_sort_v2 equal data sort function."""
    tim_sort_list = sorting.tim_sort_v2(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert tim_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_tim_sort_v2_multiple(list_inputs, expected_answer):
    """Check the tim_sort_v2 function with multiple inputs."""
    sorted_list = sorting.tim_sort_v2(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([10, 3, 1], [1, 3, 10])],
)
def test_tim_sort_v2_single(list_inputs, expected_answer):
    """Check the tim_sort_v2 function with one input."""
    sorted_list = sorting.tim_sort_v2(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_python_sort_benchmark(benchmark):
    """Benchmark the python_sort function."""
    sorted_list = benchmark(sorting.python_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@pytest.mark.benchmark
def test_wiggle_sort_benchmark(benchmark):
    """Benchmark the wiggle_sort function."""
    sorted_list = benchmark(sorting.wiggle_sort, thelist=[3, 5, 2, 1, 6, 4])
    assert sorted_list == [3, 5, 1, 6, 2, 4]


@pytest.mark.benchmark
def test_quick_sort_benchmark(benchmark):
    """Benchmark the quick_sort function."""
    sorted_list = benchmark(sorting.quick_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_quick_sort_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted using quick_sort is equal data."""
    quick_sort_list = sorting.quick_sort(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert quick_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_quick_sort_multiple(list_inputs, expected_answer):
    """Check the quick_sort function with multiple inputs."""
    sorted_list = sorting.quick_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_random_quick_sort_benchmark(benchmark):
    """Benchmark the random_quick_sort function."""
    sorted_list = benchmark(sorting.random_quick_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_random_quick_sort_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted with random_quick_sort equal sort."""
    quick_sort_list = sorting.random_quick_sort(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert quick_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_random_quick_sort_multiple(list_inputs, expected_answer):
    """Check the random_quick_sort function with multiple inputs."""
    sorted_list = sorting.random_quick_sort(list_inputs)
    assert sorted_list == expected_answer


@pytest.mark.benchmark
def test_intro_sort_benchmark(benchmark):
    """Benchmark the intro_sort function."""
    sorted_list = benchmark(sorting.intro_sort, thelist=[4, 2, 3, 1])
    assert sorted_list == [1, 2, 3, 4]


@given(list_inputs=lists(elements=integers(min_value=1, max_value=10), min_size=2))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_intro_sort_hypothesis_integer_lists_yes(list_inputs):
    """Check list of hypothesis-generated data sorted using intro_sort equal to sort function."""
    intro_sort_list = sorting.intro_sort(list_inputs)
    python_sort_list = sorted(list_inputs)
    assert intro_sort_list == python_sort_list


@pytest.mark.parametrize(
    "list_inputs, expected_answer",
    [([5, 3, 9, 2, 1], [1, 2, 3, 5, 9]), ([7, 2, 10, 3, 1], [1, 2, 3, 7, 10])],
)
def test_intro_sort_multiple(list_inputs, expected_answer):
    """Check the intro_sort function with multiple inputs."""
    sorted_list = sorting.intro_sort(list_inputs)
    assert sorted_list == expected_answer
