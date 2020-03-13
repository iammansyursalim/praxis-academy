from container import Readers,Clients,Configs

if __name__ == '__main__':
    Configs.config.override({
        "domain_name": "imap.gmail.com",
        "email_address": "sayaorang522@gmail.com",
        "password": "namasaya123",
        "mailbox": "INBOX"
    })
    email_reader = Readers.email_reader()
    print(email_reader.read())