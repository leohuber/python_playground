import ckanapi


class Config:
    def __init__(self, base_url: str) -> None:
        self._base_url = base_url
        self._client = ckanapi.RemoteCKAN(base_url)

    @property
    def base_url(self) -> str:
        return self._base_url

    @property
    def client(self) -> ckanapi.RemoteCKAN:
        return self._client


def get_organisations(config: Config, search_string: str = "") -> list[str] | None:
    try:
        # Call the organization_list action to get a list of all organizations.
        orgs: list[str] = config.client.action.organization_list()
        orgs_filtered = [org for org in orgs if search_string in org]
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching organizations:", e)
        return None
    else:
        return orgs_filtered


def get_groups(config: Config, search_string: str = "") -> list[str] | None:
    try:
        # Call the group_list action to get a list of all groups.
        groups: list[str] = config.client.action.group_list()
        groups_filtered = [group for group in groups if search_string in group]
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching groups:", e)
        return None
    else:
        return groups_filtered


def get_tags(config: Config, search_string: str = "") -> list[str] | None:
    try:
        # Call the tag_list action to get a list of all tags.
        tags: list[str] = config.client.action.tag_list()
        tags_filtered = [tag for tag in tags if search_string in tag]
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching tags:", e)
        return None
    else:
        return tags_filtered


def get_organization_details(config: Config, organization_id: str) -> dict | None:
    try:
        # Call the organization_show action to get details of a specific organization.
        org_details: dict = config.client.action.organization_show(id=organization_id)
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching organization details:", e)
        return None
    else:
        return org_details


def package_search(config: Config, search_string: str = "", filter_criterias: list[str] | None = None) -> list[dict] | None:
    try:
        # Call the package_search action to search for packages based on a search string.
        search_results: dict = config.client.action.package_search(q=search_string, fq_list=filter_criterias)
        packages: list[dict] = search_results.get("results", [])
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while searching for packages:", e)
        return None
    else:
        return packages


def get_package_details(config: Config, package_id: str) -> dict | None:
    try:
        # Call the package_show action to get details of a specific package.
        package_details: dict = config.client.action.package_show(id=package_id)
    except ckanapi.errors.CKANAPIError as e:
        print("An error occurred while fetching package details:", e)
        return None
    else:
        return package_details
