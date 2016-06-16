from {{ cookiecutter.repo_name }}._version import get_version

__all__ = ('__version__',)
__version__ = get_version()