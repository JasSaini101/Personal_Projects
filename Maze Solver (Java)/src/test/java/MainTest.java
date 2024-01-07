import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;


import java.util.ArrayList;
import java.util.List;


import static org.junit.jupiter.api.Assertions.assertEquals;


class MainTest {

    static Maze m1, m2;

    @BeforeAll
    static void setup(){
        m1 = new Maze(2,"[[0,0]]", "[1,0]","[0,1]");
        m2 = new Maze(4, "[[1,1],[2,3],[0,3],[2,1],[0,2]]", "[0,0]", "[1,3]");
    }

    @Test
    void solveMazeTest1() {

        List<Direction> ans = Main.solveMaze(m1, 100);
        ArrayList<Direction> correct = new ArrayList<>(2);
        correct.add(Direction.RIGHT);
        correct.add(Direction.UP);
        assertEquals(correct, ans);
        //System.out.println(ans);
        //System.out.println(PartialSolution.expandCount);
    }

    @Test
    void solveMazeTest2() {
        List<Direction> ans = Main.solveMaze(m2, 100);
        Direction[] steps = {Direction.DOWN, Direction.DOWN, Direction.DOWN, Direction.RIGHT, Direction.RIGHT, Direction.UP, Direction.UP, Direction.RIGHT};
        ArrayList<Direction> correct = new ArrayList<>(List.of(steps));
        assertEquals(correct, ans);
        //System.out.println(ans); //
        //System.out.println(PartialSolution.expandCount);
    }
    @Test
    void solveMazeHelper() {
    }
}



