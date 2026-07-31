# Проект: Юнит-тестирование приложения BooksCollector

Проект содержит набор автоматизированных unit-тестов для проверки функциональности класса `BooksCollector` с использованием фреймворка `pytest`.

## Описание реализованных тестов

1. `test_add_new_book_valid_name_length_success` — проверяет добавление книги с допустимой длиной названия (1 и 40 символов).
2. `test_add_new_book_invalid_name_length_not_added` — проверяет, что книги с недопустимой длиной названия (0 и 41 символ) не добавляются.
3. `test_add_new_book_duplicate_not_added` — проверяет невозможность повторного добавления одной и той же книги.
4. `test_set_book_genre_valid_genre_success` — проверяет установку жанра для существующей книги из списка доступных.
5. `test_set_book_genre_invalid_genre_not_set` — проверяет, что невалидный жанр не устанавливается.
6. `test_get_books_with_specific_genre_returns_correct_list` — проверяет фильтрацию книг по жанру.
7. `test_get_books_genre_returns_dictionary` — проверяет получение текущего словаря `books_genre`.
8. `test_get_books_for_children_excludes_age_restricted_genres` — проверяет исключение жанров с возрастным рейтингом ('Ужасы', 'Детективы').
9. `test_add_book_in_favorites_success` — проверяет добавление книги в избранное.
10. `test_add_book_in_favorites_re_addition_not_allowed` — проверяет защиту от повторного добавления в избранное.
11. `test_delete_book_from_favorites_success` — проверяет удаление книги из избранного.
12. `test_get_list_of_favorites_books_returns_favorites` — проверяет получение списка избранного.

## Запуск тестов

```bash
pytest -v tests.py
