from unittest import TestCase
from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH, CLEARED_MEMORY
from test.plugins.ReqTracer import requirements
import git_utils
import subprocess
from test.plugins.ReqTracer import jobStory
import mock

"""
#0100 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'

#0101 The system shall return one of the following when asked 'What is the status of <file path>?'

         - <file path> has been modified locally

         - <file path> has not been checked in

         - <file path> is a dirty repo

         - <file path> is up to date

#0102 The system shall return '<hash>, <date modified>, <author>' when asked 'What is the deal with <file path>?'

#0103 The system shall return the repo branch when asked 'What branch is <file path>?'

#0104 The system shall return the repo url when asked 'Where did <file path> come from?'
"""

class TestGitUtils(TestCase):

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_dirty(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = git_utils.get_git_file_info("C:\\Users\\paul ivanovs")
        self.assertEqual(result, 'paul ivanovs is a dirty repo')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = git_utils.is_file_in_repo("C:\\Users\\paul ivanovs\\PavelI.txt")
        self.assertEqual(result, 'No')


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = git_utils.get_git_file_info("C:\\Users\\paul ivanovs\\PavelI")
        self.assertEqual(result, 'PavelI is a dirty repo')


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = git_utils.get_git_file_info("C:\\Users\\paul ivanovs\\PavelI")
        self.assertEqual(result, 'PavelI is a dirty repo')


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = git_utils.get_git_file_info("C:\\Users\\paul ivanovs\\PavelI")
        self.assertEqual(result, 'PavelI is a dirty repo')
