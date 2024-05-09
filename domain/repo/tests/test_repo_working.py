import unittest
from bootstrap import Bootstrap
from kink import di
from domain.repo.repo_working_interface import IRepoWorking
from os import getenv


class TestRepoWorking(unittest.TestCase):
    def testGetTreeDirectory(self):
        bootstrap = Bootstrap()
        repo_working = di[IRepoWorking]
        repo_working.setRepoDir(getenv("REPO_DIR"))
        tree = repo_working.getTreeDirectory("repo_test", "master")
        print(tree)

    def testGetBlobFile(self):
        bootstrap = Bootstrap()
        repo_working = di[IRepoWorking]
        repo_working.setRepoDir(getenv("REPO_DIR"))
        blob = repo_working.getBlobFile("repo_test", "master", "Readme.md")
        print(blob)

    def testGetCommit(self):
        bootstrap = Bootstrap()
        repo_working = di[IRepoWorking]
        repo_working.setRepoDir(getenv("REPO_DIR"))
        commits = repo_working.listCommit("repo_test", "master")
        print(commits)


if __name__ == "__main__":
    unittest.main()
