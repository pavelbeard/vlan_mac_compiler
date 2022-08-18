import os
import pip
import difflib
import pkg_resources

__name__ = 'setup.py'


def main():
    # installed_pkgs = set(sorted(["%s==%s" % (pkg.key, pkg.version) for pkg in pkg_resources.working_set]))
    # requirements = set([pkg.replace('\n', '') for pkg in open(os.getcwd() + '\\reqs.txt').readlines()])
    #
    # to_install = installed_pkgs.intersection(requirements)

    packages = os.listdir(os.getcwd())
    for package in packages:
        if package.__contains__(".txt"):
            continue
        pip.main(["install", "--no-index", "--find-links=.", package])


if __name__ == 'setup.py':
    main()
    print('packages is installed')
