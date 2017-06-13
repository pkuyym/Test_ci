# Copyright PaddlePaddle contributors. All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
import unittest
import sys
sys.path.append('..')
import error_rate


class TestParse(unittest.TestCase):
    def test_wer(self):
        ref = 'i UM the PHONE IS i LEFT THE portable PHONE UPSTAIRS last night'
        hyp = 'i GOT IT TO the FULLEST i LOVE TO portable FROM OF STORES last night'
        word_error_rate = error_rate.wer(ref, hyp)
        self.assertTrue(abs(word_error_rate - 0.769230769231) < 1e-6)

    def test_cer_en(self):
        ref = 'werewolf'
        hyp = 'were   wolf'
        char_error_rate = error_rate.cer(ref, hyp)
        self.assertTrue(abs(char_error_rate - 0.125) < 1e-6)


if __name__ == '__main__':
    unittest.main()
