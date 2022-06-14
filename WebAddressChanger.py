class WebAddressChanger():
    """Class that change website address for file name"""

    def __init__(self, raw_address):
        self.raw_address = raw_address
        self.address_list = []

    def address_generator(self):
        """Function that generates changed website address"""
        slash_indexes = self._slash_indexer()
        ra_list = self._address_spreader()

        if slash_indexes[-1] + 1 < len(ra_list):

            self.address_list = ra_list[slash_indexes[1] + 1: slash_indexes[2]] + ra_list[slash_indexes[-1]:]
            address = str("".join(self.address_list))
            address = address.replace("/", "_")

        else:
            self.address_list = ra_list[slash_indexes[1] + 1: slash_indexes[2]] + ra_list[slash_indexes[-1] + 1:]
            address = str("".join(self.address_list))

        return address

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


address_for_fix = "https://stackoverflow.com/questions/23238352/create-object-from-class-in-separate-file"

fix = WebAddressChanger(address_for_fix)
fix.address_generator()



