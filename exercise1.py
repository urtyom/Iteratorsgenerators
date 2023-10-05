class FlatIterator:

  def __init__(self, list_of_list):
    self.list_of_list = list_of_list

  def __iter__(self):
    self.count = 0
    self.count_l = -1
    self.list_of_list[self.count]
    return self

  def __next__(self):
    if self.count_l < (len(self.list_of_list[self.count])-1):
      self.count_l += 1
    else:
      self.count_l = 0
      if self.count == (len(self.list_of_list)-1):
        raise StopIteration
      else:
        self.count += 1
    return self.list_of_list[self.count][self.count_l]


def test_1():

  list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]

  flat_list = [item for item in FlatIterator(list_of_lists_1)]

  for flat_iterator_item, check_item in zip(
    flat_list,
    ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
  ):

    assert flat_iterator_item == check_item

  assert list(flat_list) == ['a', 'b', 'c',
                             'd', 'e', 'f', 'h', False,
                             1, 2, None]
