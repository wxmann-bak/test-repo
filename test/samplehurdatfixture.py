import datetime
from tcdata import BasinHistory, StormId, BestTrackPoint

__author__ = 'tangz'

sample_hurdat = BasinHistory('dummy')
# combined snippets from real BT data
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 3, 18, 0), ident='', status='TD', lat=10.8,
                                lon=18.0, windspd=25, pres=1007)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 4, 6, 0), ident='', status='TS', lat=12.0,
                                lon=22.3, windspd=35, pres=1004)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 6, 0, 0), ident='', status='HU', lat=14.5,
                                lon=33.2, windspd=65, pres=987)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 23, 0, 0), ident='', status='HU', lat=48.3,
                                lon=39.5, windspd=65, pres=987)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 23, 6, 0), ident='', status='TS', lat=50.7,
                                lon=36.8, windspd=55, pres=994)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 23, 12, 0), ident='', status='EX', lat=53.2,
                                lon=35.4, windspd=45, pres=997)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=3, year=2000, name='ALBERTO', raw='AL032000'),
                                timestamp=datetime.datetime(2000, 8, 23, 18, 0), ident='', status='EX', lat=57.0,
                                lon=34.0, windspd=45, pres=997)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=4, year=2000, name='UNNAMED', raw='AL042000'),
                                timestamp=datetime.datetime(2000, 8, 8, 12, 0), ident='', status='TD', lat=28.2,
                                lon=74.2, windspd=30, pres=1011)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=4, year=2000, name='UNNAMED', raw='AL042000'),
                                timestamp=datetime.datetime(2000, 8, 8, 18, 0), ident='', status='TD', lat=28.1,
                                lon=75.1, windspd=30, pres=1010)
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=4, year=2000, name='UNNAMED', raw='AL042000'),
                                timestamp=datetime.datetime(2000, 8, 9, 0, 0), ident='', status='TD', lat=28.0,
                                lon=76.0, windspd=30, pres=1010)
# add 2004
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=1, year=2004, name='ALBERTO', raw='AL012004'),
                                timestamp=datetime.datetime(2004, 8, 23, 0, 0), ident='', status='HU', lat=48.3,
                                lon=39.5, windspd=65, pres=987)
# add Cat 5
sample_hurdat += BestTrackPoint(storm=StormId(basin='AL', number=1, year=2004, name='ALBERTO', raw='AL012004'),
                                timestamp=datetime.datetime(2004, 8, 24, 0, 0), ident='', status='HU', lat=48.3,
                                lon=39.5, windspd=145, pres=987)