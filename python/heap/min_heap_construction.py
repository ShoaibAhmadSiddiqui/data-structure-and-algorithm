import random
from math import floor
import pytest as pytest


class MinHeap:
    def __init__(self, array, sift_down=True):
        self.heap = array
        if sift_down:
            self.heap = self.build_heap_using_sift_down()
        else:
            self.heap = self.build_heap_using_sift_up()

    def build_heap_using_sift_down(self):
        last_parent = floor((len(self.heap) - 2) / 2)
        for last_parent in reversed(range(last_parent + 1)):
            self.sift_down(last_parent)

        return self.heap

    def build_heap_using_sift_up(self):
        first_parent = 0
        child_index = 0
        while child_index < len(self.heap):
            self.sift_up(first_parent)
            first_parent += 1
            child_index = (2 * first_parent) + 1

        return self.heap

    def sift_down(self, i):
        descendant = self.get_min_value_index(i, self.heap)
        if descendant == -1:
            return

        self.swap(i, descendant, self.heap)

        if descendant < len(self.heap):
            return self.sift_down(descendant)
        else:
            return

    def sift_up(self, i):

        descendant = self.get_min_value_index(i, self.heap)
        if descendant == -1:
            return

        self.swap(i, descendant, self.heap)

        if i == 0:
            return
        elif i == 1:
            ancestor = 0
        else:
            ancestor = floor((i - 1) / 2)
        if ancestor >= 0:
            return self.sift_up(ancestor)

    def peek(self):
        if self.heap:
            print(f"Peek {self.heap[0]}")
            print(self.heap)
            return self.heap[0]

    def remove(self):
        if self.heap:
            self.swap(0, len(self.heap) - 1, self.heap)
            value = self.heap.pop()

            first_parent = 0
            child_index = 0
            while child_index < len(self.heap):
                self.sift_up(first_parent)
                first_parent += 1
                child_index = (2 * first_parent) + 1

            print(f"Removed {value}")
            print(self.heap)
            return value
        else:
            print("Heap is empty!")
            return

    def insert(self, value):
        self.heap.append(value)
        last_parent = 0
        if len(self.heap) > 2:
            last_parent = floor((len(self.heap) - 2) / 2)
        for last_parent in reversed(range(last_parent + 1)):
            self.sift_down(last_parent)

        print(f"Inserted {value}")
        print(self.heap)

    @staticmethod
    def is_constructed(heap):
        for i, value in enumerate(heap):
            child_index1 = (2 * i) + 1
            child_index2 = (2 * i) + 2
            if child_index1 < len(heap) and child_index2 < len(heap):
                child_value1 = heap[child_index1]
                child_value2 = heap[child_index2]
                if value <= child_value1 and value <= child_value2:
                    continue
                return False
            if child_index1 < len(heap):
                child_value1 = heap[child_index1]
                if value <= child_value1:
                    continue
                return False
            if child_index1 >= len(heap) and child_index2 >= len(heap):
                return True
        return True

    @staticmethod
    def get_min_value_index(i, heap):
        min_value_index = -1
        parent_value = heap[i]
        child_index1 = (2 * i) + 1
        child_index2 = (2 * i) + 2

        if child_index1 < len(heap) and child_index2 < len(heap):
            child_value1 = heap[child_index1]
            child_value2 = heap[child_index2]
            if child_value1 <= child_value2 and parent_value >= child_value1:
                min_value_index = child_index1
            elif child_value2 <= child_value1 and parent_value >= child_value2:
                min_value_index = child_index2
        elif child_index1 < len(heap):
            child_value1 = heap[child_index1]
            if parent_value >= child_value1:
                min_value_index = child_index1

        return min_value_index

    @staticmethod
    def swap(i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


@pytest.fixture()
def test_data():
    array1 = [9, 7, 11, 5, 10, 12, 8]
    array2 = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]
    array3 = [-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8]
    array4 = [-7, 2, 3]

    return [array1, array2, array3, array4]


class TestMinHeap:

    def test_min_heap_construction_using_sift_down(self, test_data):
        result = []
        for data in test_data:
            min_heap = MinHeap(data, True)
            is_constructed = min_heap.is_constructed(min_heap.heap)
            result.append(is_constructed)
        assert all(result)

    def test_min_heap_construction_using_sift_up(self, test_data):
        result = []
        for data in test_data:
            min_heap = MinHeap(data, False)
            is_constructed = min_heap.is_constructed(min_heap.heap)
            result.append(is_constructed)
        assert all(result)

    def test_min_heap_remove_element(self, test_data):
        result = []
        for data in test_data:
            min_heap = MinHeap(data, False)
            min_heap.remove()
            is_constructed = min_heap.is_constructed(min_heap.heap)
            result.append(is_constructed)
        assert all(result)

    def test_min_heap_insert_element(self, test_data):
        result = []
        for data in test_data:
            min_heap = MinHeap(data, True)
            number = 1 + round(random.random() * 99)
            min_heap.insert(number)
            is_constructed = min_heap.is_constructed(min_heap.heap)
            result.append(is_constructed)
        assert all(result)
