import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class PathTest {
    static Maze m1, m2;
    static Path p1, p2;

    @BeforeAll
    static void setup(){
        m1 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        p1 = new Path(m1);
        m2 = new Maze(3,"[[0,0]]", "[1,0]","[0,1]");
        p2 = new Path(m2);
        System.out.println(m1);
        System.out.println(m2);
        System.out.println(p1);
        System.out.println(p2);
    }

    @Test
    void testEquals() {
        assertTrue(p1.equals(p2));
    }

    @Test
    void evalPathTest() {
        assertEquals(5, p1.evalPath(m1));
    }

    @Test
    void moveTestLeft() {
        Path p3 = new Path(m1);
        Assertions.assertThrows(UnableToMoveException.class, ()->
                p3.move(m1, Direction.LEFT));
    }
    @Test
    void moveTestDown() {
        Path p3 = new Path(m1);
        Assertions.assertThrows(UnableToMoveException.class,
                ()-> p3.move(m1, Direction.DOWN));
    }
    @Test
    void moveTestRight() throws UnableToMoveException {
        Path p3 = new Path(m1);
        p3 = p3.move(m1, Direction.RIGHT);
        assertEquals(2, p3.size());
    }
    @Test
    void moveTestUp() throws UnableToMoveException {
        Path p3 = new Path(m1);
        Assertions.assertThrows(UnableToMoveException.class,
                ()->p3.move(m1, Direction.UP)); //UP is blocked
    }

    @Test
    void isPathFoundTest() throws UnableToMoveException {
        Path p3 = new Path(m1);
        assertFalse(p3.isSolutionPath(m1));
        p3 = p3.move(m1, Direction.RIGHT);
        p3 = p3.move(m1, Direction.UP);

        assertTrue(p3.isSolutionPath(m1));
    }

    @Test
    void isNotRetracingTest() {
        Path p1 = new Path(m1);
        System.out.println("isNotRetracingTest" + p1.getPathString());
        p1.push(new Square(2,2));
        assertTrue(p1.isNotRetracing());
        p1.push(new Square(2,2));
        System.out.println("isNotRetracingTest after 2nd push" + p1.getPathString());
        assertFalse(p1.isNotRetracing());

    }
}

