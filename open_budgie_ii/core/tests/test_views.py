from django.urls import reverse
from open_budgie_ii.core.views import index


class TestIndex:
    def test_unauthenticated(self, client):
        """
        Test that an unauthenticated user gets a valid response.
        """

        response = client.get(reverse('index'))
        assert response.status_code == 200
