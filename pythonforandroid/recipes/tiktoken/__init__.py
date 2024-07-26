from pythonforandroid.recipe import RustCompiledComponentsRecipe


class TiktokenRecipe(RustCompiledComponentsRecipe):
    version = '0.7.0'
    url = 'https://pypi.python.org/packages/source/t/tiktoken/tiktoken-{version}.tar.gz'
    site_packages_name = "tiktoken"


recipe = TiktokenRecipe()