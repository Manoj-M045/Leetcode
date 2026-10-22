class Solution {
    public String removeDuplicates(String s) {
        Stack<Character>st=new Stack<>();
        if(s.isEmpty()){
            return "";
        }
        char first=s.charAt(0);
        st.push(first);
        for(int i=1;i<s.length();i++){
            char ch=s.charAt(i);
            if(!st.isEmpty() && ch==st.peek()){
                st.pop();
            }
            else{
                st.push(ch);
            }
            }
        
        StringBuilder result=new StringBuilder();
        for(int i=0;i<st.size();i++){
            result.append(st.get(i));
        }
        return result.toString();
    }
}