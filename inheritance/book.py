class Chapter:
    def __init__(self, name):
        self.name = name

    def name_of_chapter(self):
        return self.name


class Book:
    def __init__(self, book_name, chapter_name):
        self.book_name = book_name
        self.obj_chapter = Chapter(chapter_name)

    def chapter_name(self):
        return self.obj_chapter.name_of_chapter()


book = Book('Python', 'Introduction')

print(book.book_name, book.chapter_name())
