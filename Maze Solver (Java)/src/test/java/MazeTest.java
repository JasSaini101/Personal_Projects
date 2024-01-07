import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

import static org.junit.jupiter.api.Assertions.*;

class MazeTest {
    static Maze m1;

    @BeforeAll
    static void setup(){

        m1 = new Maze(4, "[[2,2],[3,4],[1,4],[3,2],[1,3]]", "[1,1]", "[2,3]");

    }

    @Test
    void parseSquareTest1() {
        String s1 = "2,3],]";
        Square exp = new Square(2,3);
        assertEquals(exp.toString(), Maze.parseSquare(s1).toString());
    }
    @Test
    void parseSquareTest2() {
        String s1 = "1,2],";
        Square exp = new Square(1,2);
        assertEquals(exp.toString(), Maze.parseSquare(s1).toString());
    }
    @Test
    void parseSquareTest3() {
        String s1 = "3,4]]";
        Square exp = new Square(3,4);
        assertEquals(exp.toString(), Maze.parseSquare(s1).toString());
    }
    @Test
    void parseSquareTest4() {
        String s1 = "[3,4]";
        Square exp = new Square(3,4);
        assertEquals(exp.toString(), Maze.parseSquare(s1).toString());
    }

    //makeMaze(4, [[2, 2],[3, 4],[1, 4],[3, 2],[1, 3]], [1, 1], [3, 3])
    @Test
    void parseSquareListTest() {
        String sqStr = "[[2, 2],[3, 4],[1, 4],[3, 2],[1, 3]], ";
        ArrayList<Square> ans = Maze.parseSquareList(sqStr);
        assertEquals(5, ans.size());
    }
    @Test
    void parseSquareListTest_Empty() {
        String sqStr = "[], ";
        ArrayList<Square> ans = Maze.parseSquareList(sqStr);
        assertEquals(0, ans.size());
    }

    @Test
    void evalSquare() {
    }

    @Test
    void countBlockedSquares() {
    }

    @Test
    void distance() {
    }

    @Test
    void squareAdjacentTest() {
    }

    @Test
    void testToString() {
        Maze m = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        assertEquals("B E \nS _ \n", m.toString() );
    }

    @Test
    void isBlockedSquareTest() {
        assertTrue(m1.isBlockedSquare(new Square(1, 3)));
        assertFalse(m1.isBlockedSquare(new Square(1, 1)));
    }
}