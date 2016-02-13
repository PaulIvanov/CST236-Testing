from unittest import TestCase
from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH, CLEARED_MEMORY
from test.plugins.ReqTracer import requirements
import source.git_utils
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

    # get_git_file_info
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_dirty(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info("C:\\Users\\paul ivanovs")
        self.assertEqual(result, 'paul ivanovs is a dirty repo')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_untracked(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'answers.pyc', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info("C:\\Users\\paul ivanovs\\PavelI\\CST236\\source\\answers.pyc")
        self.assertEqual(result, 'is untracked')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_abs_path_Yes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo("run_tests.py")
        self.assertEqual(result, 'Yes')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_abs_path_No(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo("main_test.pyc")
        self.assertEqual(result, 'Yes')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_no(self, mock_subproc_popen):
        file_path = 'C:\\Users\\paul ivanovs\\PavelI\\CST236\\'
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {file_path, 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(file_path)
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_up_to_date(self, mock_subproc_popen):
        process_mock = mock.Mock()
        process_mock.configure_mock()
        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info("C:\\Users\\paul ivanovs")
        self.assertEqual(result, 'paul ivanovs is up to date')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_modified_locally(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'C:\\Users\\paul ivanovs\\PavelI\\coverage config.txt', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info("C:\\Users\\paul ivanovs\\PavelI\\coverage config.txt")
        self.assertEqual(result, 'coverage config.txt has been modified locally')


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_invalid(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        self.assertRaisesRegexp(Exception, "Path {} does not exist".format("C"), source.git_utils.get_git_file_info, 'C')




    # is_repo_dirty
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_repo_dirty_Clean(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'', 'Error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_repo_dirty("C:\\Users\\paul ivanovs\\PavelI")
        self.assertEqual(result, False)


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_yes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, 'Yes')


    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_no(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo("C:\\Users\\paul ivanovs\\PavelI.txt")
        self.assertEqual(result, 'No')


    # get_repo_root
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_root(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'C:\\Users\\paul ivanovs\\PavelI', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_repo_root("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, 'C:\\Users\\paul ivanovs\\PavelI')


    # get_repo_branch
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_branch(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_repo_branch("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, 'master')

    # get_repo_ur
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_url(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_repo_url("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, 'master')


    # has_untracked_files
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_untracked_files_none(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'output.txt', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.has_untracked_files("C:\\Users\\paul ivanovs\\PavelI")
        self.assertEqual(result, True)

    # get_file_info
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_file_info_valid(self, mock_subproc_popen):
        process_mock = mock.Mock()
        # '<hash>, <date modified>, <author>'
        attrs = {'communicate.return_value': {'#AO56QU, 1/2/2016, PaulIvanov', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_file_info("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, '#AO56QU, 1/2/2016, PaulIvanov')


