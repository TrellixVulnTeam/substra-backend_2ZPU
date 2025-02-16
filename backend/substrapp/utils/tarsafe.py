import os
import pathlib
import tarfile


class TarSafe(tarfile.TarFile):
    """
    A safe subclass of the TarFile class for interacting with tar files.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.directory = os.getcwd()

    @classmethod
    def open(cls, name=None, mode="r", fileobj=None, bufsize=tarfile.RECORDSIZE, **kwargs):
        return super().open(name, mode, fileobj, bufsize, **kwargs)

    def extract(self, member, path="", set_attrs=True, *, numeric_owner=False):
        """
        Override the parent extract method and add safety checks.
        """
        self._safetar_check()
        super().extract(member, path, set_attrs=set_attrs, numeric_owner=numeric_owner)

    def extractall(self, path=".", members=None, numeric_owner=False):
        """
        Override the parent extractall method and add safety checks.
        """
        self._safetar_check()
        super().extractall(path, members, numeric_owner=numeric_owner)

    def _safetar_check(self):

        """
        Runs all necessary checks for the safety of a tarfile.
        """
        for tarinfo in self.__iter__():
            if self._is_traversal_attempt(tarinfo=tarinfo):
                raise TarSafeError(f"Attempted directory traversal for member: {tarinfo.name}")
            if tarinfo.issym():
                raise TarSafeError(f"Unsupported symlink for member: {tarinfo.linkname}")
            if self._is_unsafe_link(tarinfo=tarinfo):
                raise TarSafeError(f"Attempted directory traversal via link for member: {tarinfo.linkname}")
            if self._is_device(tarinfo=tarinfo):
                raise TarSafeError("tarfile returns true for isblk() or ischr()")

    def _is_traversal_attempt(self, tarinfo):
        if not os.path.abspath(os.path.join(self.directory, tarinfo.name)).startswith(self.directory):
            return True
        return False

    def _is_unsafe_link(self, tarinfo):
        if tarinfo.islnk():
            link_file = pathlib.Path(os.path.normpath(os.path.join(self.directory, tarinfo.linkname)))
            if not os.path.abspath(os.path.join(self.directory, link_file)).startswith(self.directory):
                return True
        return False

    def _is_device(self, tarinfo):
        return tarinfo.ischr() or tarinfo.isblk()


class TarSafeError(Exception):
    pass


open = TarSafe.open
