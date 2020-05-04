from setuptools import setup, find_packages

setup(
    name="rvd-tools",
    version="0.9",
    packages=find_packages(),
    include_package_data=True,  # this requires a MANIFEST.in
    install_requires=[
        "arrow",
        "bs4",
        "cerberus",
        "Click",
        "dedupe",
        "mergedeep",
        "numpy",
        "plotly",
        "PyGithub",
        "python-dateutil==2.7.3",
        "python-gitlab",
        "pyyaml",
        "qprompt",
        "tabulate",
        "vulners",
        "xmltodict",
        "pprint",
        "pygithub",
        "retrying",
        "dedupe",
        "jsonschema",
        # 'pycvesearch',  # needs to be installed manually, see https://github.com/cve-search/PyCVESearch
        # 'cvsslib',  # needs to be installed manually, see https://github.com/aliasrobotics/RVSS
    ],
    url="https://github.com/aliasrobotics/RVD",
    project_urls={"Source Code": "https://github.com/aliasrobotics/RVD"},
    license="GPLv3",
    author="Alias Robotics",
    author_email="contact@aliasrobotics.com",
    description="Toolset for the Robot Vulnerability Database (RVD)",
    long_description="""
    The Robot Vulnerability Database or RVD for short is an archive of
    robot vulnerabilities and bugs. This Python 3 package provides a set of tools to
    manage, operate and automate RVD.'
    """,
    keywords=["RVD", "vulnerability", "security", "tools", "ics"],
    entry_points={"console_scripts": ["rvd = rvd_tools.cli:start"]},
)
