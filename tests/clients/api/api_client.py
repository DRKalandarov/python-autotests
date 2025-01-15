from httpx import get, post, put, delete


class ApiClient:
    def __init__(self, host):
        self.host = host

    def get_resources(self, path, query_params=None, headers=None):
        try:
            return get(url=f"{self.host}/{path}", params=query_params, headers=headers)
        except Exception:
            pass

    def get_resource_by_id(self, path, id, query_params=None, headers=None):
        try:
            return get(url=f"{self.host}/{path}/{id}", params=query_params, headers=headers)
        except Exception:
            pass

    def create_resource(self, path, data, headers=None):
        try:
            return post(url=f"{self.host}/{path}", json=data, headers=headers)
        except Exception:
            pass

    def update_resource_by_id(self, path, id, data, headers=None):
        try:
            return put(url=f"{self.host}/{path}/{id}", json=data, headers=headers)
        except Exception:
            pass

    def delete_resource_by_id(self, path, id, headers=None):
        try:
            return delete(url=f"{self.host}/{path}/{id}", headers=headers)
        except Exception:
            pass
