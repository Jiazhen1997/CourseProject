
__author__ = 'Danyang'
class Solution:
    def wordBreak_TLE(self, s, dict):
        
        string_builder = ""
"" "" "" "" "" "" "" "" ""i""f"" ""s""=""=
         __       __________   ___  __    ______   ______   .__   __.      _______.
        |  |     |   ____\  \ /  / |  |  /      | /  __  \  |  \ |  |     /       |
        |  |     |  |__   \  V  /  |  | |  ,----'|  |  |  | |   \|  |    |   (----`
        |  |     |   __|   >   <   |  | |  |     |  |  |  | |  . `  |     \   \
        |  `----.|  |____ /  .  \  |  | |  `----.|  `--'  | |  |\   | .----)   |
        |_______||_______/__/ \__\ |__|  \______| \______/  |__| \__| |_______/

        Dynamic programming
        The dynamic solution can tell us whether the string can be broken to words, but can not tell us what words the string is broken to.

        O(n*m)
        Google On Campus Presentation, demonstration questions. 4 Sep 2014, Nanyang Technological University, Singapore

        dp[i] rolling dp (rather than using 2D dp[i, j]
        dp[i] means s[:i] can be made up of sequence of lexicons
        - l e e t c o d e
        T F F F T F F F T

        Lexicons = {the, theta, table, down, there, bled, own}
        - t h e t a b l e d o w n t h e r e
        T F F T F T F F T T F F T F F F F T

        :param s: a string
        :param dict: a set of string
        :return: a boolean
        