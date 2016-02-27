from unittest import TestCase
from source.main import Interface, NOT_A_QUESTION_RETURN, UNKNOWN_QUESTION, NO_QUESTION, NO_TEACH, CLEARED_MEMORY
from test.plugins.ReqTracer import requirements
import source.git_utils
import subprocess
from test.plugins.ReqTracer import jobStory
import mock
import os
import time

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
        result = source.git_utils.get_git_file_info(os.path.dirname(__file__))
        self.assertEqual(result, 'test is a dirty repo')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_untracked(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.side_effect': [('', 'empty'), ('','empty'), ('git_utils_test.py','onefile'), (__file__, '4'), ('duh', '5'), ('poo','6')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(os.path.relpath(__file__ + 'lol'))
        self.assertEqual(result, 'No')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_untracked(self, mock_subproc_popen):
        process_mock = mock.Mock()
        testpath = os.path.dirname(__file__)
        attrs = {'communicate.side_effect': [('', 'empty'), ('', 'empty'), ('git_utils_test.pyc','empty'), (testpath,'onefile'), (testpath, '4'), ('duh', '5'), ('poo','6'), ('', '7'), ('', '8')]}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info(os.path.relpath(__file__))
        self.assertEqual(result, 'git_utils_test.pyc has been not been checked in')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_abs_path_Yes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {' ', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo("run_tests.py")
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_abs_path_No(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(os.path.relpath(__file__))
        self.assertEqual(result, 'Yes')

    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_no(self, mock_subproc_popen):
        file_path = (__file__ + 'lol')
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
        result = source.git_utils.get_git_file_info(__file__)
        self.assertEqual(result, 'git_utils_test.pyc is up to date')

    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_status_repo_modified_locally(self, mock_subproc_popen):
        process_mock = mock.Mock()
        modified_path = os.path.dirname(__file__)
        modified_path.join('main_test.py')
        attrs = {'communicate.return_value': {modified_path, 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_git_file_info(modified_path)
        self.assertEqual(result, 'test has been modified locally')


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
        result = source.git_utils.is_repo_dirty(__file__)
        self.assertEqual(result, False)


    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_yes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(__file__)
        self.assertEqual(result, 'Yes')


    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_is_file_in_repo_no(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {__file__, 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.is_file_in_repo(__file__)
        self.assertEqual(result, 'No')


    # get_repo_root
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_root(self, mock_subproc_popen):
        process_mock = mock.Mock()
        modified_path = os.path.dirname(__file__)
        attrs = {'communicate.return_value': {modified_path, 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_repo_root("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, modified_path)


    # get_repo_branch
    @requirements(['#0103'])
    @mock.patch('subprocess.Popen')
    def test_get_repo_branch(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_repo_branch("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, 'master')

    # get_repo_ur
    @requirements(['#0104'])
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
    @requirements(['#0102'])
    @mock.patch('subprocess.Popen')
    def test_get_file_info_valid(self, mock_subproc_popen):
        process_mock = mock.Mock()
        # '<hash>, <date modified>, <author>'
        attrs = {'communicate.return_value': {'#AO56QU, 1/2/2016, PaulIvanov', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = source.git_utils.get_file_info("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        self.assertEqual(result, '#AO56QU, 1/2/2016, PaulIvanov')


    # get_git_file_info
    @requirements(['#0100'])
    @mock.patch('subprocess.Popen')
    def test_ask_is_file_in_repo(self, mock_subproc_popen):
        test_question = 'Is the {} in the repo?'.format('C:\\Users\\paul_ivanovs\\PavelI\\README.md')
        process_mock = mock.Mock()
        my_interface = Interface()

        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, 'No')


    # get_git_file_info
    @requirements(['#0101'])
    @mock.patch('subprocess.Popen')
    def test_what_is_status_of_repo_up_to_date(self, mock_subproc_popen):
        test_question = 'What is the status of {}?'.format(__file__)
        process_mock = mock.Mock()
        my_interface = Interface()

        attrs = {'communicate.return_value': {'', 'error'}}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, 'git_utils_test.pyc is up to date')


    # get_git_file_info
    @requirements(['#0102'])
    @mock.patch('subprocess.Popen')
    def test_what_is_status_of_repo_hashes(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'#AO56QU, 1/2/2016, PaulIvanov', 'error'}}
        process_mock.configure_mock(**attrs)
        test_question = 'What is the deal with {}?'.format("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, '#AO56QU, 1/2/2016, PaulIvanov')


    # get_git_file_info
    @requirements(['#0103'])
    @mock.patch('subprocess.Popen')
    def test_what_is_branch_name(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        test_question = 'What branch is {}?'.format("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, 'master')

    # get_git_file_info
    @requirements(['#0104'])
    @mock.patch('subprocess.Popen')
    def test_what_is_repo_url(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        test_question = 'Where did {} come from?'.format("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, 'master')


    @requirements(['#0104', '#0050', '#0051', '#0052'])
    @mock.patch('subprocess.Popen')
    def test_what_is_repo_url(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'communicate.return_value': {'master', 'error'}}
        process_mock.configure_mock(**attrs)
        test_question = 'Where did {} come from?'.format("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        result = my_interface.ask(test_question)
        self.assertEqual(result, 'master')

    @requirements(['#0050', '#0051', '#0052'])
    @mock.patch('source.git_utils.get_repo_root')
    def test_what_is_repo_url_log(self, mock_subproc_popen):
        process_mock = mock.Mock()
        attrs = {'get_repo_root.return_value': 'C:\\Users\\paul ivanovs\\PavelI\\README.md'}
        process_mock.configure_mock(**attrs)
        test_question = 'Where did {} come from?'.format("C:\\Users\\paul ivanovs\\PavelI\\README.md")
        my_interface = Interface()
        mock_subproc_popen.return_value = process_mock
        time0 = time.clock()
        result = my_interface.ask(test_question)
        time1 = time.clock()

        delta_time = time1 - time0

        self.assertLessEqual(delta_time, 0.050)
