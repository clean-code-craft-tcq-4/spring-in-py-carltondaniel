import unittest
import sys
#sys.path.append('C:\\Users\\CQN1KOR\\')
import statistics 
from statistics import EmailAlert,LEDAlert,StatsAlerter
import math



class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):    
    computedStats = statistics.calculateStats([])
    self.assertEqual(computedStats["avg"],str(math.nan))
    self.assertEqual(computedStats["max"],str(math.nan))
    self.assertEqual(computedStats["min"],str(math.nan))

    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Design the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_raise_alerts_when_max_above_threshold(self):
    emailAlert = EmailAlert()
    ledAlert = LEDAlert()
    maxThreshold = 10.5
    statsAlerter = StatsAlerter(maxThreshold, [emailAlert, ledAlert])
    statsAlerter.checkAndAlert([22.6, 12.5, 3.7])
    self.assertTrue(emailAlert.emailSent,"No Email Alert")
    self.assertTrue(ledAlert.ledGlows,"No Led Alert")

if __name__ == "__main__":

  unittest.main()
