import unittest
def merge_ranges(meetings):
    l2=meetings
    l.sort()
    l1=[]
    temp=-1
    count=0
    for i in range(len(l2)-1):
        if(len(l2[i])==0):
            l1.append((1,l2[i+1][1]))
            continue
        if(l2[i+1][0]<=l2[i][1]):
            if(count==0):
                temp=l2[i][0]
                count+=1
            if(i==len(l2)-2):
                if(l2[i-count+1][1]>l2[i+1][1]):
                    l1.append((l2[i-count+1][0],l2[i-count+1][1]))
                else:
                    l1.append((l2[i-count+1][0],l2[i+1][1]))
        else:
            if(l2[i-count][0]==temp):
                l1.append((l2[i-count][0],l2[i][1]))
                count=0
                temp=-1
            else:
                if(i+2==len(l2)):
                    l1.append(l2[i])
                    l1.append(l2[i+1])
                else:
                    l1.append(l2[i])
    return l1

class Test(unittest.TestCase):

    def test_meetings_overlap(self):
        actual = merge_ranges([(1, 3), (2, 4)])
        expected = [(1, 4)]
        self.assertEqual(actual, expected)

    def test_meetings_touch(self):
        actual = merge_ranges([(5, 6), (6, 8)])
        expected = [(5, 8)]
        self.assertEqual(actual, expected)

    def test_meeting_contains_other_meeting(self):
        actual = merge_ranges([(1, 8), (2, 5)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_stay_separate(self):
        actual = merge_ranges([(1, 3), (4, 8)])
        expected = [(1, 3), (4, 8)]
        self.assertEqual(actual, expected)

    def test_multiple_merged_meetings(self):
        actual = merge_ranges([(          ), (5, 8)])
        expected = [(1, 8)]
        self.assertEqual(actual, expected)

    def test_meetings_not_sorted(self):
        actual = merge_ranges([(5, 8), (1, 4), (6, 8)])
        expected = [(1, 4), (5, 8)]
        self.assertEqual(actual, expected)

    def test_sample_input(self):
        actual = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
        expected = [(0, 1), (3, 8), (9, 12)]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
