"""
This modules includes all the functions that are used very frequently.
"""

import os
import shutil
import re

def get_nodevers_prefix():
    """
    Return the path where Nodes will be installed
    and configuration will be created.
    """
    nodevers_prefix = os.getenv("NODEVERS_PREFIX")
    if nodevers_prefix is not None:
        return nodevers_prefix
    elif os.geteuid() == 0:
        return "/opt/nodist"
    else:
        home_path = os.getenv("HOME")
        return os.path.join(home_path, ".nodevers")

def valid_nodist_prefix(path):
    """
    Check if path exists and if it has the required subdirs:
        versions/
        tmp/
        patches/
        patches/global
    """
    dirs = ["versions", "tmp", "patches", os.path.join("patches", "global")]
    for i in dirs:
        full_path = os.path.join(path, i)
        if not os.path.isdir(full_path):
            return False
    return True

def mknodist_prefix(path):
    """
    Removes the path if it exists and then creates the directories
    needed by nodevers.
    """
    if os.path.exists(path):
        shutil.rmtree(path)
    dirs = ["versions", "tmp", "patches", os.path.join("patches", "global")]
    for i in dirs:
        full_path = os.path.join(path, i)
        os.makedirs(full_path)

def valid_version_string(version):
    """
    Use regex to see if version
    looks valid.
    """
    regex = "^(\d+)\.(\d+)\.(\d+)$"
    match = re.match(regex, version)
    if match is None:
        return False
    else:
        return True

def get_versions_dir():
    """
    Return the path where Nodes will be installed.
    """
    return os.path.join(get_nodevers_prefix(), "versions")

def get_bin_dir():
    """
    Return the path where the symlink to current Node's bin
    will be created.
    """
    return os.path.join(get_nodevers_prefix(), "bin")

def get_patches_dir():
    """
    Return the path where the user should put his patches in.
    """
    return os.path.join(get_nodevers_prefix(), "patches")

def get_tmp_dir():
    """
    Return the path where nodevers will download source packages
    and build Node.
    """
    return os.path.join(get_nodevers_prefix(), "tmp")
