from setuptools import find_packages, setup

setup(
    name="ServerlessTestS",
    author="Aleksandar Petaković",
    license="MIT",
    description="Serverless Unit Tests Generator",
    keywords="DSL, Serverless, Lambda, Unit, Test",
    url="https://github.com/saksofon997/serverless-unit-tests-dsl",
    long_description="file: README.md",
    long_description_content_type="text/markdown",
    version="0.1.1",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "": ["*.tx", "sts_generator/**/*.template", "sts_generator/**/*.py"]},
    install_requires=["Arpeggio", "textX[cli]", "Jinja2", "future", "textX"],
    entry_points={
        "textx_commands": [
            "sts-generate = sts_generator.main:sts_generate"
        ],
        "textx_languages": [
            "serverless_unit_test_dsl = sts_generator.main:serverless_unit_test_dsl",
        ],
        "textx_generators": [
            "serverless_unit_test_dsl_test = sts_generator.main:tests_generator",
            "serverless_unit_test_dsl_dot = sts_generator.main:dot_generator"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers"
    ],
)
