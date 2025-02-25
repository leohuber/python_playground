#!/usr/bin/env python3
import ckanapi

class Config:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._client = ckanapi.RemoteCKAN(base_url)

    @property
    def base_url(self):
        return self._base_url
    
    @property
    def client(self):
        return self._client

def get_organisations(config: Config, search_string:str) -> list[str]:
    try:
        # Call the organization_list action to get a list of all organizations.
        orgs: list[str] = config.client.action.organization_list()
        orgs_filtered = [org for org in orgs if search_string in org]
        return orgs_filtered
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching organizations:", e)
        return []
