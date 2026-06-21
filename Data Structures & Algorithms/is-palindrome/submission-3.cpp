
class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0, j = (int)s.size() - 1;
        while (i < j) {
            // skip non-alnum
            while (i < j && !std::isalnum((unsigned char)s[i])) ++i;
            while (i < j && !std::isalnum((unsigned char)s[j])) --j;

            if (i >= j) break;

            char a = std::tolower((unsigned char)s[i]);
            char b = std::tolower((unsigned char)s[j]);
            if (a != b) return false;

            ++i; --j;
        }
        return true;
    }
};