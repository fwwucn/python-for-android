from pythonforandroid.recipe import RustCompiledComponentsRecipe


class OrjsonRecipe(RustCompiledComponentsRecipe):
    version = '3.10.6'
    url = 'https://pypi.python.org/packages/source/o/orjson/orjson-{version}.tar.gz'
    site_packages_name = 'orjson'


recipe = OrjsonRecipe()