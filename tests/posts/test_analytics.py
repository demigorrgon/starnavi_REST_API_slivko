import pytest
from django.urls import reverse

pytestmark = [pytest.mark.django_db]


def test_analytics_with_valid_dates(api_client_with_token, dummy_post):
    like_url = reverse("posts-like", args=[f"{dummy_post.pk}"])
    api_client_with_token.post(like_url)
    url = "/api/analytics/?date_from=2022-07-24&date_to=2022-07-26"
    response = api_client_with_token.get(url)
    assert "There was 1" in response.data.get("response")
    assert response.status_code == 200


def test_analytics_no_likes(api_client_with_token, dummy_post):
    url = "/api/analytics/?date_from=2022-07-24&date_to=2022-07-25"
    response = api_client_with_token.get(url)
    assert "There are no likes" in response.data.get("response")
    assert response.status_code == 200
