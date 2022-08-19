#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from typing import List

from cdp_backend.pipeline.ingestion_models import EventIngestionModel
from cdp_scrapers.legistar_utils import LegistarScraper

###############################################################################


def get_events(
    from_dt: datetime,
    to_dt: datetime,
    **kwargs,
) -> List[EventIngestionModel]:
    scraper = LegistarScraper(
        client="mountainview",
        timezone="America/Los_Angeles",
        ignore_minutes_item_patterns=[
            (
                "During this declared state of emergency, "
                "the meeting will be conducted in accordance"
            ),
            "the City Council participated in the meeting by video conference",
            (
                "There is a 90-day limit for the filing of a challenge "
                "in Superior Court to certain City administrative decisions"
            ),
            "CONSENT CALENDAR - None.",
            "During this declared state of emergency",
        ],
    )

    return scraper.get_events(begin=from_dt, end=to_dt)
