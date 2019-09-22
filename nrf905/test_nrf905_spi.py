#!/usr/bin/env python3

import pigpio
import unittest
import sys

from nrf905.nrf905_spi import Nrf905Spi


def callback(data):
    """ Prints out the contents of the data received. """
    print("callback", data)
    print()


class TestNrf905Spi(unittest.TestCase):
    
    def setUp(self):
        self.pi = pigpio.pi()
        self.spi = Nrf905Spi(self.pi, 0)

    def tearDown(self):
        self.spi.close(self.pi)
        self.pi.stop()

    def test_configuration_register_read_write(self):
        """ Verify that the defaults can be read.
        Verify that certain values can be modified.
        """
        # Test defaults
        data = self.spi.configuration_register_read(self.pi)
        self.assertEqual(len(data), 10)
        self.spi.configuration_register_print(data)
        # # Modify values.
        # frequency_mhz = 433.2
        # rx_address = 0xABABABAB
        # crc_bits = 8
        # config_register = self.spi.configuration_register_create(frequency_mhz, rx_address, crc_bits)
        # self.spi.configuration_register_write(self.pi, config_register)
        # # Verify changes have been written. 
        # data = self.spi.configuration_register_read(self.pi)
        # self.assertEqual(len(data), 10)
        # self.spi.configuration_register_print(data)

    # def test_transmit_address_read_write(self):
        # """ Verify that the functions that write to and read from the TX_ADDRESS
        # register work as expected. """
        # # Verify that default value, E7E7E7E7, can be read.
        # address = self.spi.read_transmit_address(self.pi)
        # expected_address = 0xE7E7E7E7
        # print("Expected address", expected_address, "actual address", address)
        # # self.assertEqual(address, expected_address)
        # self.assertEqual(0, self.spi.get_status_register())


if __name__ == '__main__':
    unittest.main()
