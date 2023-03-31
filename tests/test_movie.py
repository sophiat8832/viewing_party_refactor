import pytest
from viewing_party.movie import Movie

def test_that_name_genre_title_is_truthy():
    # Arrange/Act
    movie1 = Movie("Titanic", "Drama", 4)
    
    # Assert
    assert movie1.name == "Titanic"
    assert movie1.genre == "Drama"
    assert movie1.rating == 4