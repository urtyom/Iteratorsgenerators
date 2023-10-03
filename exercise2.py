import types


def flat_generator(list_of_lists):

  count = 0
  while True:
    for i in list_of_lists[count]:
      yield i
    count += 1
    if count == len(list_of_lists):
      break

def test_2():

  list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
  ]

  for flat_iterator_item, check_item in zip(
      flat_generator(list_of_lists_1),
      ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
  ):

      assert flat_iterator_item == check_item

  assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c',
                                                   'd', 'e', 'f', 'h', False,
                                                   1, 2, None]

  assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
