from __future__ import annotations

import platform
import shutil
import subprocess


# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program: str) -> str | None:
    """Get the path of the passed binary

    Search the PATH for the given binary name.
    Mimics the UNIX `which` command

    :param program: The name of the binary
    :type program: str
    :return: The binary's path (or None if the binary isn't found)
    :rtype: str | None
    """
    import os

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, _ = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


# TODO: See if this new [builtin] module can replace the existing function
def which_new(program: str) -> str | None:
    """Get the path of the passed binary

    Search the PATH for the given binary name.
    Mimics the UNIX `which` command

    :param program: The name of the binary
    :type program: str
    :return: The binary's path (or None if the binary isn't found)
    :rtype: str | None
    """
    return shutil.which(program)


# TODO: could this be replaced with `if 'localhost' in url`?
def is_localhost_url(url: str) -> bool:
    """Check if a URL is a localhost URL

    Check if the hostname of the URL contains only "localhost" or "localhost" and a port.

    :param url: The URL to check.
    :type url: str
    :return: True if the url is a localhost URL, False otherwise
    :rtype: bool
    """
    return "://localhost/" in url or "://localhost:" in url


def get_system() -> str:
    """Get the `system` string

    :return: The `system` string
    :rtype str
    :raises: NotImplementedError
    """
    plat = platform.system().lower()
    if plat not in ["windows", "linux", "darwin"]:
        raise NotImplementedError(f"Unsupported platform: {plat}")
    return plat


def get_architecture() -> str:
    """Get the `architecture` string

    :return: The `architecture` string
    :rtype str
    :raises: NotImplementedError
    """
    arch = platform.machine().lower()
    if arch in ["x86_64", "amd64"]:
        arch = "amd64"
    elif arch in ["arm64", "aarch64"]:
        arch = "arm64"
    elif arch.startswith("arm"):
        arch = "arm"
    else:
        raise NotImplementedError(f"Unsupported architecture: {arch}")

    return arch


def open_in_browser(url: str) -> None:
    """Open the passed URL in a browser
    :param url: The URL to open
    :type url: str
    :return: None
    :rtype: None
    """
    if get_system() == "windows":
        # FIXME: explorer.exe is the file explorer. Should this be MS Edge instead?
        subprocess.run(["explorer.exe", url])
    else:
        subprocess.run(["open", url])
