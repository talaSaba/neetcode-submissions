/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
  ListNode* d = nullptr; // start with an empty reversed list

    while(head!=nullptr)
    {
        ListNode* j=new ListNode(head->val);
        j->next=d;
        d=j;
        head=head->next;


    }
    
        
   return d; }
};
