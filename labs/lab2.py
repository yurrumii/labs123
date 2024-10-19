# TODO Найдите количество книг, которое можно разместить на дискете
memory_megabyte = 1.44
pages = 100
lines = 50
chars_line = 25
char = 4
memory_byte = memory_megabyte * 1024 * 1024
volume_of_the_book = pages * lines * chars_line * char
books_on_memory = memory_byte//volume_of_the_book
print("Количество книг, помещающихся на дискету:",int (books_on_memory) )


