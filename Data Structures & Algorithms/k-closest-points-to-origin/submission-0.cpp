#include <cmath>

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // unordered_map<int, vector<pair<int, int>>> distance_map;
        // priority_queue<pair<double, vector<int>>, vector<pair<double, vector<int>>>, less<double>> pq;
        priority_queue<pair<double, vector<int>>> pq;
        vector<vector<int>> return_arr;

        double dist, pq_top_dist;
        pair<double, vector<int>> pq_top;
        vector<int> pq_top_cords;
        // vector<vector<int, int>> pq_top_cords;
        for (auto const & point : points){
            dist = calc_dist(point);
            if (pq.size() < k){
                pq.push({dist, point});
            }
            else{
                pq_top = pq.top();
                pq_top_dist = pq_top.first;
                pq_top_cords = pq_top.second;
                if (dist < pq_top_dist) {
                    pq.pop();
                    pq.push({dist, point});
                }
                // else if (dist == pq_top_dist) {
                //     pq_top_cords.push_back(point);
                //     pq.pop();
                //     pq.push(dist, pq_top_cords);
                // }
            }
        }

        // for (auto const & _, cord : pq){
        //     return_arr.push_back(cord);
        // }

        while (!pq.empty()){
            return_arr.push_back(pq.top().second);
            pq.pop();
        }


        return return_arr;
    }

    double calc_dist(const vector<int>& p1, const vector<int>& p2 = {0, 0}){
        int x1 = p1[0], y1= p1[1], x2 = p2[0], y2 = p2[1];
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
    }
};
