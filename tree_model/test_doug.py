import numpy as np
import pandas as pd
from collections import Counter

def perfect_score(truth_y):

    score = 0
    for i in range(truth_y.shape[0]):
        if truth_y[i] == 3: score += 0.25
        else: score += 0.75

    return score

def test():

    df = pd.read_csv('test.csv')
    targets = ['agree', 'disagree', 'discuss', 'unrelated']
    targets_dict = dict(zip(targets, range(len(targets))))
    df['target'] = map(lambda x: targets_dict[x], df['Stance'])
    y = df['target'].values
    print perfect_score(y)
    print Counter(y)

if __name__ == '__main__':
    test()

 #   Copyright 2017 Cisco Systems, Inc.
 #
 #   Licensed under the Apache License, Version 2.0 (the "License");
 #   you may not use this file except in compliance with the License.
 #   You may obtain a copy of the License at
 #
 #     http://www.apache.org/licenses/LICENSE-2.0
 #
 #   Unless required by applicable law or agreed to in writing, software
 #   distributed under the License is distributed on an "AS IS" BASIS,
 #   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 #   See the License for the specific language governing permissions and
 #   limitations under the License.
