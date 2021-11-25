
class CheckArguments:
    def __init__(self, args):
        self.args = args

    def check_arguments_count(self):
        if len(self.args) == 1 or len(self.args) > 3:
            self.print_arg_error()
        else:
            return True

    def return_arguments(self):
        if len(self.args) == 2:
            self.args.append('')
        self.args = self.args[1:]

    def print_arg_error(self):
        print()
        print('Za malo argumentow.') if len(self.args) == 1 \
            else print('Za duzo argumentow.')
        print('Wywolanie programu:')
        print('\tweather.py <klucz_do_API> [<data>]')
        print()
        print('Przy braku daty program sprawdza pogode na jutro.')
        return False
