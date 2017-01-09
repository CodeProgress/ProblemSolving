
def insert_at_all_positions(bookmark, book):
    new_books = []
    for bookmark_position in range(len(book)):
        new_book_config = book[:bookmark_position] + bookmark + book[bookmark_position:]
        new_books.append(new_book_config)
    new_books.append(book + bookmark)    # include bookmark at end of book
    return new_books

def permutations(a_str):
    if len(a_str) <= 1:
        return [a_str]
    
    perms = []
    previous_perms = permutations(a_str[:-1])
    for book in previous_perms:
        bookmark = a_str[-1]
        for new_perm in insert_at_all_positions(bookmark, book):
            perms.append(new_perm)
    return perms

assert permutations('') == ['']
assert permutations('a') == ['a']
assert set(permutations('ab')) == set(['ab', 'ba'])
assert set(permutations('abc')) == set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
assert len(permutations('abcd')) == 24
assert len(permutations('abcde')) == 120
assert len(permutations('abcdef')) == 720
# assert len(permutations('abcdefg')) == 5040
# assert len(permutations('abcdefgh')) == 40320
# assert len(permutations('abcdefghi')) == 362880

print permutations('abc')