class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if set(name) != set(typed):
            return False
        def compress_split_string(str_):
            char_counter = 1
            str_ += ' '
            list_compress = []
            for idx, t_char in enumerate(str_):
                if idx == 0:
                    continue
                if t_char != str_[idx - 1]:
                    list_compress.append(str_[idx - 1] + str(char_counter))
                    char_counter = 1
                else:
                    char_counter += 1
            return list_compress
        name_compress = compress_split_string(name)
        typed_compress = compress_split_string(typed)
        if len(name_compress) != len(typed_compress):
            return False
        for n_num, t_num in zip(name_compress, typed_compress):
            if t_num < n_num:
                return False
        return True