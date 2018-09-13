# -*- coding: utf-8 -*-
import logging as logger
import re
from datetime import datetime, timedelta
from urllib.parse import urlparse, parse_qs

import feedparser
import requests
from bs4 import BeautifulSoup


class CSWeb:
    def __init__(self, url='https://cs.kaist.ac.kr/rss/events/ko'):
        self.url = url
        self.feed = feedparser.parse(url)

    @staticmethod
    def _url_to_event_id(url):
        return parse_qs(urlparse(url).query)['bbs_sn'][0]

    def get_event_ids(self, refresh=False):
        # refresh feed?
        if refresh:
            self.feed = feedparser.parse(self.url)

        return [self._url_to_event_id(entry['link'])
                for entry in self.feed.entries]

    def get_event_details(self, event_id):
        """
        Returns: title, location, description, start_dt, end_dt
        """
        title, location, description, start_dt, end_dt = None, None, None, None, None

        logger.warning('Fetching event: {}'.format(event_id))

        # exception: 8447 (seems a stray event)
        if event_id == '8447':
            return title, location, description, start_dt, end_dt

        # title, description
        for entry in self.feed.entries:
            if event_id == self._url_to_event_id(entry['link']):
                title = entry['title']
                description = entry['description']

        url_pattern = 'https://cs.kaist.ac.kr/board/view?bbs_id=events&bbs_sn={}&menu=86'
        r = requests.get(url_pattern.format(event_id))
        soup = BeautifulSoup(r.text, 'html.parser')

        # start_dt, end_dt
        dt_info = soup.find('p', class_='seminarsInfo').text.split('\n')[1].split('@')
        date_str = dt_info[0].strip()

        time_info = dt_info[1].strip().split('~')

        start_time = time_info[0]
        start_dt_str = '{} @ {}'.format(date_str, start_time)
        start_dt = datetime.strptime(start_dt_str, '%a, %b %d, %Y @ %H:%M')

        if len(time_info) == 2:
            end_time = time_info[1]
            end_dt_str = '{} @ {}'.format(date_str, end_time)
            end_dt = datetime.strptime(end_dt_str, '%a, %b %d, %Y @ %H:%M')
        else:
            # assume 1hr 30m event
            end_dt = start_dt + timedelta(hours=1, minutes=30)

        # location
        location = soup.find('strong', text=re.compile('Location:*')).text.split(':')[-1].strip()

        return title, location, description, start_dt, end_dt
