
class main_generator:

    def __init__(self, pwd_min=8, pwd_max=12, out_file="passwords.txt"):
        self.names = names_perm
        self.dates = dates_perm
        self.oldpwds = oldpwds_perm
        self.total_result = []

        self.pwd_max = pwd_max
        self.pwd_min = pwd_min

        self.out_file = out_file


    def __valid_pwd(self, pwd):
        if (len(pwd) >= self.pwd_min) and (len(pwd) <= self.pwd_max) and (pwd not in self.total_result):
            return True
        return False

    def __export(self):
        if (self.total_result):
            sys.stdout.write(f"[*] Exporting results to {self.export_file}...\n")
            sys.stdout.flush()
            with open(self.out_file, "w") as f:
                for pwd in self.total_result:
                    f.write(f"{pwd}\n")
            print(f"[+] Results exported to {self.export_file}!")

    def __input(self):
        result = []
        data = input()
        if data:
            for part in data.split(',')
            result.append(part)

        return result

    def perms_generator():
        pass

    def interface(self):
        self.names = self.names(self.__input("Any names: "))
        self.dates = self.dates(self.__input("Any special dates (Format: [dd-mm-yy]): "))
        self.oldpwds = self.oldpwds(self.__input("Any old passwords or keywords: "))

        self.perms_generator()
