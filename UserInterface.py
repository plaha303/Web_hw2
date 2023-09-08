from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, contact_name, notes):
        pass

    @abstractmethod
    def display_commands(self, commands):
        pass


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        res = ""
        for contact in contacts:
            res += f"Name: {contact['name']} \n" \
                   f"Phones: {', '.join(contact['phones'])} \n" \
                   f"Birthday: {contact['birthday']} \n" \
                   f"Email: {contact['email']} \n" \
                   f"Status: {contact['status']} \n" \
                   f"Note: {contact['note']} \n"
        return res

    def display_notes(self, contact_name, notes):
        pass

    def display_commands(self, commands):
        res = "Commands: \n"
        format_str = str('{:%s%d}' % ('^', 20))
        for command in commands:
            res += f"{format_str.format(command)}\n"
        return res
