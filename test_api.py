"""test api"""

from unittest import IsolatedAsyncioTestCase
from unittest.mock import Mock

from api import get_people_factory


class TestGetPeopleFactory(IsolatedAsyncioTestCase):
    """test get_people_factory"""

    async def test_empty(self) -> None:
        """empty"""
        get_people = Mock(return_value=[])

        endpoint_fn = get_people_factory(get_people)

        people = await endpoint_fn()

        with self.subTest("empty result"):
            self.assertCountEqual((), people)

        with self.subTest("calls get_people"):
            get_people.assert_called_once()

    async def test_parse_set_of_people(self) -> None:
        """parse set of people"""

        endpoint_fn = get_people_factory(
            lambda: [
                (5, "Thomas", "Riker"),
                (42, "Kathryn", "Janeway"),
            ]
        )

        people = await endpoint_fn()

        self.assertCountEqual(
            (
                {"uid": 5, "first_name": "Thomas", "last_name": "Riker"},
                {"uid": 42, "first_name": "Kathryn", "last_name": "Janeway"},
            ),
            people,
        )
