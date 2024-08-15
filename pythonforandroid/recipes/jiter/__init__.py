from pythonforandroid.recipe import RustCompiledComponentsRecipe


class JiterRecipe(RustCompiledComponentsRecipe):
    version = '0.5.0'
    url = 'https://pypi.python.org/packages/source/j/jiter/jiter-{version}.tar.gz'
    site_packages_name = 'jiter'


recipe = JiterRecipe()
