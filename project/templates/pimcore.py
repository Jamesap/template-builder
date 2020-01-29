from project import RemoteProject


class Pimcore(RemoteProject):
    major_version = "v1"
    remote = "https://github.com/pimcore/skeleton.git"

    @property
    def platformify(self):
        return super(Pimcore, self).platformify + [
            "cd {0} && composer update --no-scripts && composer require platformsh/config-reader doctrine/orm --ignore-platform-reqs --no-scripts".format(
                self.builddir
            ),
        ]


__all__ = ("Pimcore",)
