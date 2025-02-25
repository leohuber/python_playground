#!/usr/bin/env python3
"""

--> https://docs.ckan.org/en/latest/api/index.html#module-ckan.logic.action.get

This module provides a simple interface to interact with CKAN API to fetch organizations.
Classes:
    Config: A configuration class to initialize CKAN API client.
Functions:
    get_organisations(config: Config, search_string: str) -> list[str]:
        Fetches and filters organizations from CKAN based on a search string.
        Args:
            config (Config): An instance of the Config class containing CKAN API client.
            search_string (str): The string to filter organizations by.
        Returns:
            list[str]: A list of organization names that match the search string.
        Raises:
            ckanapi.errors.CKANAPIError: If an error occurs while fetching organizations from CKAN API.
"""
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

def get_organisations(config: Config, search_string:str = "") -> list[str]:
    '''Fetches and filters organizations from CKAN based on a search string.
    Args:
        config (Config): An instance of the Config class containing CKAN API client.
        search_string (str): The string to filter organizations by.
    Returns:
        list[str]: A list of organization names that match the search string.
    '''
    try:
        # Call the organization_list action to get a list of all organizations.
        orgs: list[str] = config.client.action.organization_list()
        orgs_filtered = [org for org in orgs if search_string in org]
        return orgs_filtered
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching organizations:", e)
        return []
    
def get_groups(config: Config, search_string:str = "") -> list[str]:
    '''Fetches and filters groups from CKAN based on a search string.
    Args:
        config (Config): An instance of the Config class containing CKAN API client.
        search_string (str): The string to filter groups by.
    Returns:
        list[str]: A list of groups that match the search string.
    '''
    try:
        # Call the group_list action to get a list of all groups.
        groups: list[str] = config.client.action.group_list()
        groups_filtered = [group for group in groups if search_string in group]
        return groups_filtered
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching groups:", e)
        return []
    
def get_tags(config: Config, search_string:str = "") -> list[str]:
    '''Fetches and filters tags from CKAN based on a search string.
    Args:
        config (Config): An instance of the Config class containing CKAN API client.
        search_string (str): The string to filter tags by.
    Returns:
        list[str]: A list of tags that match the search string.
    '''
    try:
        # Call the tag_list action to get a list of all tags.
        tags: list[str] = config.client.action.tag_list()
        tags_filtered = [tag for tag in tags if search_string in tag]
        return tags_filtered
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching tags:", e)
        return []
    
def get_organization_details(config: Config, organization_id: str) -> dict:
    '''Fetches details of a specific organization from CKAN based on the organization ID.
    Args:
        config (Config): An instance of the Config class containing CKAN API client.
        organization_id (str): The ID of the organization to fetch details for.
    Returns:
        dict: A dictionary containing details of the organization.
    '''
    try:
        # Call the organization_show action to get details of a specific organization.
        org_details: dict = config.client.action.organization_show(id=organization_id)
        return org_details
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching organization details:", e)
        return {}
    
def package_search(config: Config, search_string:str = "") -> list[dict]:
    '''Searches for packages on CKAN based on a search string.
    Args:
        config (Config): An instance of the Config class containing CKAN API client.
        search_string (str): The string to search for in package names.
    Returns:
        list[dict]: A list of dictionaries containing details of packages that match the search string.
    '''
    try:
        # Call the package_search action to search for packages based on a search string.
        search_results: dict = config.client.action.package_search(q=search_string)
        packages: list[dict] = search_results.get('results', [])
        return packages
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while searching for packages:", e)
        return []
