from django.core.management.base import BaseCommand
import unittest as ut
import consumption.models as cm
import dashboard.settings
import os, csv, datetime

class Command(BaseCommand):
    help = 'import data'

    def handle(self, *args, **options):
        #  Read user data
        self.import_user_data(os.path.join(os.path.dirname(
            dashboard.settings.BASE_DIR), "data", "user_data.csv"))
        for user in self.users:
            self.import_user_consumption_data(user)

    def import_user_consumption_data(self, user):
        consumption_data = []
        #  Read user's consumption data
        with open(os.path.join(self.base_dir, "consumption",
                               str(user.id) + ".csv")) as consumption_data_file:
            self.stdout.write("Reading " + consumption_data_file.name)
            consumption_reader = csv.DictReader(consumption_data_file)
            for consumption_record in consumption_reader:
                time = datetime.datetime.strptime(consumption_record['datetime'],
                                                  "%Y-%m-%d %H:%M:%S")
                #  Create consumption object
                consumption = cm.Consumption(user = user,
                                             time = time,
                                             units = float(consumption_record['consumption']))
                #  Store for later bulk insert.
                consumption_data.append(consumption)
        if len(consumption_data) == 0:
            self.stdout.write("\tNo consumption data found for user " +\
                              str(user.id) + "! Skipping insert and correctness test.")
            return
        self.stdout.write("\tInserting consumption data.")
        cm.Consumption.objects.bulk_create(consumption_data)
        self.stdout.write("\tDone")

        #  Test correctness
        consumption = cm.Consumption.objects.filter(user=user)
        for record, item in zip(consumption, consumption_data):
            if record.units != item.units:
                message = "Correctness test failed!\n"\
                    "Error in consumption data.\n"\
                    "\tUser: " + str(user.id) + ", time: "\
                    + record.time.strftime("%Y-%m-%d %H:%M:%S")
                raise ValueError(message)
        self.stdout.write("\tTests passed!")

    def import_user_data(self, user_data_file_path):
        self.base_dir = os.path.dirname(user_data_file_path)
        self.users = []
        with open(user_data_file_path) as user_data_file:
            self.stdout.write("Reading " + user_data_file.name)
            csv_reader = csv.DictReader(user_data_file)
            for record in csv_reader:
                #  Create User records
                self.stdout.write("\tReading user " + record['id'])
                user = cm.User(id = int(record['id']), area = record['area'],
                               tariff = record['tariff'])
                #  Store for later bulk insert.
                self.users.append(user)
        self.stdout.write("Creating users")
        cm.User.objects.bulk_create(self.users)
