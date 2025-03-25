"""
 We need to write a function that generates a dictionary from the input string.
 The data separator is the character ":"
 Example string:
 "key1: val1: key2: val2"

 "" -> {}
 "k" - > {"k": None}
 "k:" - > {"k":"}
 "key1:val1: key1" - > {"key1": ["val1", None]}
"""


def str_to_dict(input_string: str):
    def append_value(key, value):
        if key in result:
            result[key] = result[key].append(value) if isinstance(result[key], list) else [result[key], value]
        else:
            result[key] = value

    result = {}
    if len(input_string) == 0:
        return result
    splited_string = input_string.split(":")
    for i in range(1, len(splited_string) + 1 // 2, 2):
        key = splited_string[i - 1]
        value = splited_string[i]
        append_value(key, value)
    if len(splited_string) % 2 != 0:
        append_value(splited_string[-1], None)
    return result


if __name__ == '__main__':
    print(str_to_dict("key1:value1:key2:value2"))
    print(str_to_dict("key1:value1:key1:value2"))
    print(str_to_dict("key1:value1:key1"))
    print(str_to_dict("key1:"))
    print(str_to_dict("key1"))
