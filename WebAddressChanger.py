class WebAddressChanger:
    """Class that change website address for file name"""

    def __init__(self, raw_address):
        self.ra_list = None
        self.slash_indexes = None
        self.raw_address = raw_address
        self.address = ""
        self.address_list = []

    def address_generator(self):
        """Function that generates changed website address"""
        self.slash_indexes = self._slash_indexer()
        self.ra_list = self._address_spreader()

        if self.slash_indexes[-1] + 1 < len(self.ra_list):

            self.address_list = self.ra_list[self.slash_indexes[1] + 1: self.slash_indexes[2]] + self.ra_list[self.slash_indexes[-1]:]
            self.address = str("".join(self.address_list))
            self.address = self.address.replace("/", "_")

        else:
            self.address_list = self.ra_list[self.slash_indexes[1] + 1: self.slash_indexes[2]] + self.ra_list[self.slash_indexes[-1] + 1:]
            self.address = str("".join(self.address_list))

        return self.address

    def _address_spreader(self):
        """Function that spread website address string into a list"""

        ra_list = [char for char in self.raw_address]
        return ra_list

    def _slash_indexer(self):
        """Function that searches for slashes in website address"""

        slash_indexes =[]
        for i in range(len(self._address_spreader())):

            if self._address_spreader()[i] == "/":

                slash_indexes.append(i)

        return slash_indexes


