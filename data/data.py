# coding=utf-8
import collections
import time

from faker import Faker

from utils.random_helpers import RandomHelpers

fake = Faker("fi_FI")
Name = collections.namedtuple("Name", "name surname")


class Data:
    def get_my_words(self):
        return self.get_values_from_file("my_words.txt")

    def get_fake_sentence(self, nb_words):
        return fake.sentence(nb_words, ext_word_list=self.get_my_words())

    @staticmethod
    def get_fake_paragraph(nb_sentences):
        return fake.paragraph(nb_sentences)

    @staticmethod
    def get_random_name() -> Name:
        return Name(fake.first_name(), fake.last_name())

    @staticmethod
    def get_timestamp_str():
        return time.strftime("%d.%m.%Y %H:%M:%S")

    @staticmethod
    def get_values_from_file(filename) -> list:
        """This function reads variable values from given file to list."""
        path = f"{RandomHelpers().get_data_root()}/{filename}"
        with open(path) as file:
            my_variable_list = file.read().splitlines()
        return my_variable_list
