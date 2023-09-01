from .base import BaseHandler


class ConfigHandler(BaseHandler):
    """Serve config"""

    def generate_config(self):
        return {
            repo_provider_class_alias: repo_provider_class.labels
            for repo_provider_class_alias, repo_provider_class in self.settings[
                "repo_providers"
            ].items()
        }

    async def get(self):
        self.write(self.generate_config())
