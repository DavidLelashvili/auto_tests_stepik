
# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
#     assert expected_result == actual_result, \
#         f"expected {expected_result}, got {actual_result}"
#
# test_input_text(8,11)

# s = 'My Name is Julia'

# if 'Name' in s:
#     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')

def test_substring(full_string, substring):
    assert substring in full_string, \
    f"expexted '{substring}' to be of '{full_string}'"

test_substring("full_text", "some")

