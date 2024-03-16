import json
from typing import List
from app.entities.processed_agent_data import ProcessedAgentData
from app.interfaces.store_api_gateway import StoreGateway
import requests
from datetime import datetime


class StoreApiAdapter(StoreGateway):
    def __init__(self, api_base_url):
        self.api_base_url = api_base_url

    def save_data(self, processed_agent_data_batch: List[ProcessedAgentData]):
        url = f'{self.api_base_url}/processed_agent_data'

        def default_converter(o):
            if isinstance(o, datetime):
                return o.isoformat()
            raise TypeError(f"Object of type {o.__class__.__name__} is not JSON serializable")

        data_json = json.dumps([processed_agent_data.dict() for processed_agent_data in processed_agent_data_batch],
                               default=default_converter)

        requests.post(url, data=data_json)
