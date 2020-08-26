---
layout: default
title: 电话号码的字母组合
---

## [17\. 电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

> Medium

#### 思路

这道题的本质是求字母组合的全排列，转化成[全排列]那道题的思路，使用**回溯法**。只不过我们这边要多转换一步，将数字转换成是字母的可能

* 所有的选择形成一颗树状结构，使用`dfs回溯`来解
* 回溯的套路，定义一个`path`表示，当前选择的路径，定义`res`记录我们需要返回的结果，定义`curIndex`表示当前在`digits`中选择到的位置
* 选择一层之后，回溯一下，换条路继续递归。也就是将`path`的结尾元素删除
* **递归终止条件** 当`curIndex == len(digits)` 也就是选择到终点时结束

以上，尝试写一下代码，AC！

#### 代码
python3
```python
class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    dic = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'} 
    if len(digits) == 0:
      return []   
    def helper(digits, cur, path, res):
      if cur >= len(digits):
        res.append(path)
        return
      ls = dic[digits[cur]]
      for l in ls:
        helper(digits, cur+1, path+l, res)
      path = path[:-1][::]
      return 
    res = []
    helper(digits, 0, '',res)
    return res
```

C++
```cpp
class Solution {
public:
    void helper(unordered_map<char,string>& dic, string& digits, int curIndex, string path, vector<string>& res) {
      if (curIndex == digits.length()){
        res.push_back(path);
        return;
      }
      char d = digits[curIndex];
      string ls = dic.at(d);
      for(char& l: ls){
        path.push_back(l);
        helper(dic,digits,curIndex+1,path,res);
        path.pop_back();
      }
      return; 
    }

    vector<string> letterCombinations(string digits) {
      unordered_map<char,string> dic = {
        {'1',""},
        {'2',"abc"},
        {'3',"def"},
        {'4',"ghi"},
        {'5',"jkl"},
        {'6',"mno"},
        {'7',"pqrs"},
        {'8',"tuv"},
        {'9',"wxyz"},
      };

      vector<string> res = {};
      if(digits.length() == 0){
        return res;
      }
      helper(dic,digits,0,"",res);
      return res;
    }
};
```