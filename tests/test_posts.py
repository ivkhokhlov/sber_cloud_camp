from test_data.default_data import USER_ID, TITLE, BODY


def test_get_posts(placeholder_api):
    status_code, post_data = placeholder_api.get_posts()
    assert status_code == 200
    assert len(post_data) != 0


def test_get_post(placeholder_api, create_default_post):
    post_id = create_default_post
    status_code, post_data = placeholder_api.get_post(post_id)
    assert status_code == 200
    assert post_id == post_data.get('id')


def test_delete_post(placeholder_api, create_default_post):
    _, post_data = placeholder_api.create_post(user_id=USER_ID,
                                               title=TITLE,
                                               body=BODY)
    post_id = post_data.get('id')
    status_code, delete_data = placeholder_api.delete_post(post_id)
    assert status_code == 200
    assert len(delete_data) != 0

    status_code, get_deleted_data = placeholder_api.get_post(post_id)
    assert status_code == 404
    assert len(delete_data) == 0
