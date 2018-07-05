import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;
import static org.junit.Assert.*;

public class Solution 
{

    public static class LinkedListNode 
    {

        public int val;
        public LinkedListNode next;

        public LinkedListNode(int val)
         {
            this.val = val;
        }
    }
    static LinkedListNode final_node;
    public class flag
    {
        int count=0;
    }
    public LinkedListNode  kthToLastNode(int i, LinkedListNode head)
    {
        flag cou=new flag();
        LinkedListNode temp=kthToLastNode(i,head,cou);
       System.out.println(temp); 

        if(temp==null)
        {
             throw new IllegalArgumentException("invalid");
        }
        else
        {
            return temp;
        }
    }
    public static LinkedListNode kthToLastNode(int i, LinkedListNode head,flag count) {

        if(i==0)
        {
            throw new IllegalArgumentException("invalid");
        }
        if(head==null)
        {
           
           return null;
        }
        kthToLastNode(k,head.next,count);
        count.count++;
        
        if(count.count==i)
        {
            System.out.println(head.val);
            final_node=head;
        }
        
      return final_node;
       
    }

@Test
    public void firstToLastNodeTest() {
        final LinkedListNode[] listNodes = valsToLinkedListNodes(new int[] {1, 2, 3, 4});
        final int k = 1;
        final LinkedListNode actual = kthToLastNode(k, listNodes[0]);
        final LinkedListNode expected = listNodes[listNodes.length - k];
        assertSame(expected, actual);
    }

    @Test
    public void secondToLastNodeTest() {
        final LinkedListNode[] listNodes = valsToLinkedListNodes(new int[] {1, 2, 3, 4});
        final int k = 2;
        final LinkedListNode actual = kthToLastNode(k, listNodes[0]);
        final LinkedListNode expected = listNodes[listNodes.length - k];
        assertSame(expected, actual);
    }
   

    @Test
    public void firstNodeTest() {
        final LinkedListNode[] listNodes = valsToLinkedListNodes(new int[] {1, 2, 3, 4});
        final int k = 4;
       
        final LinkedListNode actual = kthToLastNode(k, listNodes[0]);
        final LinkedListNode expected = listNodes[listNodes.length - k];
        assertSame(expected, actual);
    }

   

    @Test(expected = Exception.class)
    public void kIsZeroTest() {
        final LinkedListNode[] listNodes = valsToLinkedListNodes(new int[] {1, 2, 3, 4});
        final int k = 0;
        kthToLastNode(k, listNodes[0]);
    }

    private static LinkedListNode[] valsToLinkedListNodes(int[] vals) {
        final LinkedListNode[] nodes = new LinkedListNode[vals.length];
        for (int i = 0; i < vals.length; i++) {
            nodes[i] = new LinkedListNode(vals[i]);
            if (i > 0) {
                nodes[i - 1].next = nodes[i]; 
            }
        }
        return nodes;
    }

    public static void main(String[] args) {
        Result result = JUnitCore.runClasses(Solution.class);
        for (Failure failure : result.getFailures()) {
            System.out.println(failure.toString());
        }
        if (result.wasSuccessful()) {
            System.out.println("All tests passed.");
        }
    }
}