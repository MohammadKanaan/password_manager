import project


def test_password_entry():
    assert project.password_entry(
        "google",
        "www.google.com",
        "mohammad",
        "mypass123",
        "a note",
    ) == {
        "name": "google",
        "url": "www.google.com",
        "username": "mohammad",
        "password": "mypass123",
        "note": "a note",
    }

    assert project.password_entry(
        "amazon",
        "http://www.amazon.com",
        "mohammad",
        "123456789",
        "",
    ) == {
        "name": "amazon",
        "url": "http://www.amazon.com",
        "username": "mohammad",
        "password": "123456789",
        "note": "",
    }


def test_validate_url():
    assert project.validate_url("www.amazon.com") == "https://www.amazon.com"
    assert project.validate_url("http://www.amazon.com") == "http://www.amazon.com"
    assert project.validate_url("https://www.amazon.com") == "https://www.amazon.com"


def test_read_csv():
    assert project.read_csv("test_passwords.csv", encrypted=True) == [
        {
            "name": "google",
            "url": "https://google.com",
            "username": "mohammad",
            "password": "pass",
            "note": "",
        }
    ]


def test_search():
    # search by name
    assert project.search(
        [
            {
                "name": "amazon",
                "url": "http://www.amazon.com",
                "username": "mohammad",
                "password": "pass",
                "note": "",
            }
        ],
        "name",
        "amazon",
    ) == [
        {
            "name": "amazon",
            "url": "http://www.amazon.com",
            "username": "mohammad",
            "password": "pass",
            "note": "",
        }
    ]

    # search by url
    assert project.search(
        [
            {
                "name": "amazon",
                "url": "http://www.amazon.com",
                "username": "mohammad",
                "password": "pass",
                "note": "",
            }
        ],
        "url",
        "amazon",
    ) == [
        {
            "name": "amazon",
            "url": "http://www.amazon.com",
            "username": "mohammad",
            "password": "pass",
            "note": "",
        }
    ]

    # search by username
    assert project.search(
        [
            {
                "name": "amazon",
                "url": "http://www.amazon.com",
                "username": "mohammad",
                "password": "pass",
                "note": "",
            }
        ],
        "username",
        "mohammad",
    ) == [
        {
            "name": "amazon",
            "url": "http://www.amazon.com",
            "username": "mohammad",
            "password": "pass",
            "note": "",
        }
    ]

    # not found
    assert (
        project.search(
            [
                {
                    "name": "amazon",
                    "url": "http://www.amazon.com",
                    "username": "mohammad",
                    "password": "pass",
                    "note": "",
                }
            ],
            "name",
            "google",
        )
        == []
    )


def test_encrypt():
    assert project.encrypt("pass") == "e(]]"
    assert project.encrypt("pass123") == "e(]]O&i"


def test_decrypt():
    assert project.decrypt("e(]]") == "pass"
    assert project.decrypt("e(]]O&i") == "pass123"


def test_choice_to_int():
    assert project.choice_to_int("5") == 5
    assert project.choice_to_int("text") == "Invalid"
