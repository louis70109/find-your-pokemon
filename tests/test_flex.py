import unittest
from unittest.mock import MagicMock

from utils.flex import replay_flex


class TestReplayFlex(unittest.TestCase):

    def setUp(self):
        self.sd_user_record = [
            {"uploadtime": 1682434022, "id": "gen9vgc2023regulationc-1851299369",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434023, "id": "gen9vgc2023regulationc-1851299370",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434024, "id": "gen9vgc2023regulationc-1851299371",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434025, "id": "gen9vgc2023regulationc-1851299372",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434026, "id": "gen9vgc2023regulationc-1851299373",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434027, "id": "gen9vgc2023regulationc-1851299374",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434028, "id": "gen9vgc2023regulationc-1851299375",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434029, "id": "gen9vgc2023regulationc-1851299376",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434030, "id": "gen9vgc2023regulationc-1851299377",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"},
            {"uploadtime": 1682434031, "id": "gen9vgc2023regulationc-1851299378",
                "format": "gen9vgc2023regulationc", "p1": "picleopa", "p2": "Nijiatw"}
        ]
        self.sd_user_record_length = 11

    def test_replay_flex_with_empty_sd_user_record(self):
        sd_user_record = []
        sd_user_record_length = 0
        result = replay_flex(sd_user_record, sd_user_record_length)
        self.assertIsNone(result)

    def test_replay_flex_with_one_layer_content(self):
        result = replay_flex(self.sd_user_record[:1], 1)
        self.assertEqual(result, 1)

    def test_replay_flex_with_multiple_layer_content(self):
        result = replay_flex(self.sd_user_record[:5], 5)
        self.assertEqual(result, 5)

    def test_replay_flex_with_full_sd_user_record(self):
        result = replay_flex(self.sd_user_record, self.sd_user_record_length)
        self.assertEqual(result, self.sd_user_record_length)

    def test_replay_flex_with_mocked_sd_user_record(self):
        mock_sd_user_record = MagicMock()
        mock_sd_user_record.__len__.return_value = 7
        result = replay_flex(mock_sd_user_record, 7)
        self.assertEqual(result, 7)


if __name__ == 'main':
    unittest.main()
