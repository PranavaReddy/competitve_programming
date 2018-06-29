import org.junit.Test;
import org.junit.runner.JUnitCore;
import org.junit.runner.Result;
import org.junit.runner.notification.Failure;

import static org.junit.Assert.*;

public class Solution {

    public static int fibonacci(int n) 
    {
        if(n<0)
        {
        throw new IllegalArgumentException("Negative number");
    }
         
        else if(n==0 || n==1)
            return n;
        else
            return fibonacci(n-1)+fibonacci(n-2);

    
    }


















    // tests

    @Test
    public void zerothfibonaccionacciTest() {
        final int actual = fibonacci(0);
        final int expected = 0;
        assertEquals(expected, actual);
    }

    @Test
    public void firstfibonaccionacciTest() {
        final int actual = fibonacci(1);
        final int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void secondfibonaccionacciTest() {
        final int actual = fibonacci(2);
        final int expected = 1;
        assertEquals(expected, actual);
    }

    @Test
    public void thirdfibonaccionacciTest() {
        final int actual = fibonacci(3);
        final int expected = 2;
        assertEquals(expected, actual);
    }

    @Test
    public void fifthfibonaccionacciTest() {
        final int actual = fibonacci(5);
        final int expected = 5;
        assertEquals(expected, actual);
    }

    @Test
    public void tenthfibonaccionacciTest() {
        final int actual = fibonacci(10);
        final int expected = 55;
        assertEquals(expected, actual);
    }

    @Test(expected = Exception.class)
    public void negativefibonaccionacciTest() {
        fibonacci(-1);
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

