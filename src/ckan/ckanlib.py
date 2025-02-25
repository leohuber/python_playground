#!/usr/bin/env python3
import ckanapi

class Config:
    def __init__(self, base_url: str):
        self._base_url = base_url

    @property
    def base_url(self):
        return self._base_url

def main():
    # Base URL for opendata.swiss
    base_url:str = 'https://ckan.opendata.swiss'
    
    #ckanapi.RemoteCKAN.base_url = 'api/3/action/'
    client = ckanapi.RemoteCKAN(base_url)
    
    try:
        # Call the package_list action to get a list of all package IDs.
        package_ids = client.action.package_list()
        print(f"Total packages found: {len(package_ids)}")
        print("List of package IDs:")
        for pkg_id in package_ids:
            print(f"- {pkg_id}")
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching packages:", e)

if __name__ == '__main__':
    main()
