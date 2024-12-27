import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def date_and_state() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_processing_filter(date_and_state: list):
    assert filter_by_state(date_and_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(date_and_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state([]) == []
    assert filter_by_state()


def test_processing_date(date_and_state: list):
    assert sort_by_date(date_and_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "asd"},
            {"id": 615064591, "state": "CANCELED", "date": "asd"},
            {"id": 594226727, "state": "CANCELED", "date": "asd"},
            {"id": 939719570, "state": "EXECUTED", "date": "asd"},
        ]
    ) == [
        {"id": 41428829, "state": "EXECUTED", "date": "asd"},
        {"id": 615064591, "state": "CANCELED", "date": "asd"},
        {"id": 594226727, "state": "CANCELED", "date": "asd"},
        {"id": 939719570, "state": "EXECUTED", "date": "asd"},
    ]
    assert sort_by_date([]) == []
