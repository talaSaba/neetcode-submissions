class TimeMap {
private:
    unordered_map<string, vector<pair<int, string>>> keyStore;

public:
    TimeMap() {}

    void set(string key, string value, int timestamp) {
        keyStore[key].push_back({timestamp, value});
    }

    string get(string key, int timestamp) {
        auto& values = keyStore[key];
        if (values.empty()) return "";

        int left = 0;
        int right = values.size() - 1;
        string result = "";

        // simpler version of binary search
        while (left <= right) {
            int mid = (left + right) / 2;  // simpler, still works fine here
            if (values[mid].first == timestamp) {
                return values[mid].second; // exact match found
            }
            else if (values[mid].first < timestamp) {
                result = values[mid].second;
                left = mid + 1; // move right
            }
            else {
                right = mid - 1; // move left
            }
        }

        return result;
    }
};
