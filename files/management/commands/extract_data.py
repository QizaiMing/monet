from django.core.management.base import BaseCommand, CommandError
from files.models import ControlFile, DetailFile


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file_name", type=str)

    def handle(self, *args, **options):
        file_name = options["file_name"]
        control_file_instance = None
        registry_expiry_date = None

        with open(file_name, "r") as reader:
            line = reader.readline()
            while line != "":
                if int(line[0]) == 1:
                    print("\n\n*** CONTROL FILE ***\n\n")
                    print(f"Type: {line[0]}")
                    print(f"NIT: {line[1:14]}")
                    print(f"Name: {line[14:34]}")
                    print(f"Partner Code: {int(line[34:49])}")
                    print(
                        f"Transmission Date: {line[49:53]}-{line[53:55]}-{line[55:57]}"
                    )
                    print(f"Shipping Code: {line[57:58]}")
                    print(f"Expiry Date: {line[58:62]}-{line[62:64]}-{line[64:66]}")
                    print(f"Registry Count: {int(line[66:74])}")
                    print(
                        f"Transaction Total: {float(line[74:89] + '.' + line[89:91])}"
                    )
                    print(f"Details: {line[91:170]}")
                    print("\n\n")

                    control_file = ControlFile()
                    control_file.NIT = line[1:14]
                    control_file.name = line[14:34]
                    control_file.partnership_code = int(line[34:49])
                    control_file.tranmission_date = (
                        f"{line[49:53]}-{line[53:55]}-{line[55:57]}"
                    )
                    control_file.shipping_code = line[57:58]
                    control_file.expiry_date = (
                        f"{line[58:62]}-{line[62:64]}-{line[64:66]}"
                    )
                    control_file.registry_count = int(line[66:74])
                    control_file.transactions_total = float(
                        line[74:89] + "." + line[89:91]
                    )
                    control_file.details = line[91:170]
                    control_file.save()

                    control_file_instance = control_file
                    registry_expiry_date = control_file.expiry_date

                    line = reader.readline()
                    continue

                print("\n\n*** DETAIL FILE ***\n\n")
                print(f"Type: {line[0]}")
                print(f"NIT: {line[1:14]}")
                print(f"Name: {line[14:34]}")
                print(f"Bank Account: {line[34:43]}")
                print(f"Account Number: {line[43:60]}")
                print(f"Transaction Type: {line[60:62]}")
                print(f"Transaction Amount: {float(line[62:77] + '.' + line[77:79])}")
                print(f"Validation Indicator: {line[79:80]}")
                print(f"Reference 1: {line[80:110]}")
                print(f"Reference 2: {line[110:140]}")
                print(f"Expiry Date: {line[140:144]}-{line[144:146]}-{line[146:148]}")
                print(f"Billed Period: {line[148:150]}")
                print(f"Cycle: {line[150:153]}")
                print(f"Details: {line[153:170]}")
                print("\n\n")

                detail_file = DetailFile()
                detail_file.control_file = control_file_instance
                detail_file.NIT = line[1:14]
                detail_file.name = line[14:34]
                detail_file.bank_account = line[34:43]
                detail_file.account_number = line[43:60]
                detail_file.transaction_type = line[60:62]
                detail_file.transaction_amount = float(line[62:77] + "." + line[77:79])
                detail_file.validation_indicator = line[79:80]
                detail_file.reference_1 = line[80:110]
                detail_file.reference_2 = line[110:140]

                # Expiry date is 00000000
                if line[140:148] == "00000000":
                    detail_file.expiry_date = registry_expiry_date

                else:
                    detail_file.expiry_date = (
                        f"{line[140:144]}-{line[144:146]}-{line[146:148]}"
                    )

                detail_file.billed_period = line[148:150]
                detail_file.cycle = line[150:153]
                detail_file.details = line[153:170]
                detail_file.save()

                line = reader.readline()