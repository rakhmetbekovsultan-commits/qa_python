import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    # 1. Добавление книг с допустимой длиной названия (граничные значения: 1 и 40)
    @pytest.mark.parametrize('book_name', ['А', 'А' * 40])
    def test_add_new_book_valid_name_length_success(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
        assert collector.get_books_genre()[book_name] == ''

    # 2. Невалидная длина названия книги (0 и 41 символ)
    @pytest.mark.parametrize('invalid_name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_length_not_added(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    # 3. Повторное добавление существующей книги
    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.add_new_book('Гарри Поттер')
        assert len(collector.get_books_genre()) == 1

    # 4. Установка валидного жанра из списка допустимых
    def test_set_book_genre_valid_genre_success(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_book_genre('Дюна') == 'Фантастика'

    # 5. Установка невалидного жанра
    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Роман')
        assert collector.get_book_genre('Дюна') == ''

    # 6. Получение списка книг определенного жанра
    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book('Дюна')
        collector.add_new_book('Оно')
        collector.set_book_genre('Дюна', 'Фантастика')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Дюна']

    # 7. Получение словаря books_genre
    def test_get_books_genre_returns_dictionary(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')
        assert collector.get_books_genre() == {'Дюна': 'Фантастика'}

    # 8. Получение книг для детей (без возрастных ограничений)
    def test_get_books_for_children_excludes_age_restricted_genres(self, collector):
        collector.add_new_book('Шрек')
        collector.add_new_book('Оно')
        collector.set_book_genre('Шрек', 'Мультфильмы')
        collector.set_book_genre('Оно', 'Ужасы')

        children_books = collector.get_books_for_children()
        assert 'Шрек' in children_books
        assert 'Оно' not in children_books

    # 9. Добавление книги в избранное
    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert '1984' in collector.get_list_of_favorites_books()

    # 10. Запрет повторного добавления книги в избранное
    def test_add_book_in_favorites_re_addition_not_allowed(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('1984')
        assert len(collector.get_list_of_favorites_books()) == 1

    # 11. Удаление книги из избранного
    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert '1984' not in collector.get_list_of_favorites_books()

    # 12. Получение полного списка избранного
    def test_get_list_of_favorites_books_returns_favorites(self, collector):
        collector.add_new_book('1984')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('1984')
        collector.add_book_in_favorites('Дюна')
        assert collector.get_list_of_favorites_books() == ['1984', 'Дюна']