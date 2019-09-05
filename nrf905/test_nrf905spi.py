#!/usr/bin/env python3

import pigpio
import unittest
import sys

from nRF905.nRF905_SPI import nRF905_SPI


def callback(data):
    """ Prints out the contents of the data received. """
    print("callback", data)
    print()


class TestnRF905_SPI(unittest.TestCase):

    def setUp(self):
        self.pi = pigpio.pi()
        self.spi = nRF905_SPI(self.pi)

    def tearDown(self):
        self.spi.close(self.pi)
        self.pi.stop()

    def test_configuration_register_read(self):
        data = self.spi.configuration_register_read(self.pi)
        self.assertEqual(len(data), 10)
        self.spi.configuration_register_print(data)

    def test_transmit_address_read_write(self):
        """ Verify that the functions that write to and read from the TX_ADDRESS
        register work as expected. """
        # Verify that default value, E7E7E7E7, can be read.
        address = self.spi.read_transmit_address()
        self.assertEqual(address, 0xe7e7e7e7)



if __name__ == '__main__':
    unittest.main()
