import time
from django.urls import reverse
import pytest

pytestmark = [pytest.mark.django_db]


def test_user_activity_change(api_client_with_token, test_user, dummy_post):
    like_url = reverse("posts-like", args=[f"{dummy_post.pk}"])
    # previous_datetimes = (test_user.last_login, test_user.last_activity)
    activity_url = reverse("user-activity", args=[f"{test_user.pk}"])
    previous_activity_record = api_client_with_token.get(activity_url).data
    assert previous_activity_record.get("last_login") is not None
    time.sleep(60)
    response = api_client_with_token.post(like_url)
    assert response.status_code == 200
    response = api_client_with_token.post(like_url)
    assert response.status_code == 200
    response = api_client_with_token.get(activity_url)
    current_activity_record = api_client_with_token.get(activity_url).data

    assert (
        previous_activity_record["last_login"],
        previous_activity_record["last_activity"],
    ) != (
        current_activity_record["last_login"],
        current_activity_record["last_activity"],
    )
