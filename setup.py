try:
    from setuptools import find_packages, setup  # type: ignore
except ImportError:
    # setuptools not available (e.g., in some analysis environments); provide minimal fallbacks
    # Avoid importing distutils.core which may not be available in some analysis environments.
    def find_packages():
        return []
    def setup(*args, **kwargs):
        # Minimal no-op fallback for environments without setuptools/distutils
        return None

setup(
    name = 'Generative AI Project',
    version= '0.0.0',
    author= 'Kalpana Mamella',
    author_email= 'kalpana150906@gmail.com',
    packages= find_packages(),
    install_requires = []

)