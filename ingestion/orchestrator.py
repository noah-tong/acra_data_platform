from ingestion.framework.scheduler import Scheduler

from ingestion.extractors.flight_extractor import FlightExtractor
from ingestion.extractors.airport_extractor import AirportExtractor
from ingestion.extractors.aircraft_extractor import AircraftExtractor
from ingestion.extractors.weather_extractor import WeatherExtractor
from ingestion.extractors.fuel_extractor import FuelExtractor
from ingestion.extractors.news_extractor import NewsExtractor
from ingestion.extractors.holiday_extractor import HolidayExtractor


class IngestionOrchestrator:

    def __init__(self):

        self.scheduler = Scheduler()

        self.extractors = {

            "flight": FlightExtractor(),

            "airport": AirportExtractor(),

            "weather": WeatherExtractor(),
            "fuel": FuelExtractor(),
            "news": NewsExtractor(),
            "aircraft": AircraftExtractor(),
            "holiday": HolidayExtractor(),

        }

    def run(self):

        for source, extractor in self.extractors.items():

            if self.scheduler.should_run(source):

                print(f"Running {source}...")

                extractor.run()

            else:

                print(f"Skipping {source}(not due yet)")