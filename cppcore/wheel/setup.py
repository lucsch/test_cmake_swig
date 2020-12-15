from setuptools import setup, dist
from setuptools.command.install import install

# force setuptools to recognize that this is
# actually a binary distribution
class BinaryDistribution(dist.Distribution):
    def has_ext_modules(foo):
        return True


setup(
    # this package is called modfact
    name='modfact',

    # this package contains one module,
    # which resides in the subdirectory mymodule
    # packages=['modfact'],

    scripts=["modfact"],

    # make sure the shared library is included
    package_data={"modfact": ['_modfact.pyd']},
    include_package_data=True,

    description="This is a short description",
    # optional, the contents of README.md that were read earlier

    # See class BinaryDistribution that was defined earlier
    distclass=BinaryDistribution,

    version='0.0.1',
    url='http://example.com/',
    author='...',
    author_email='...@example.com'
    # ...
)